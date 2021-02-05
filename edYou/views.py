from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.exceptions import FieldError, ObjectDoesNotExist
from django.contrib import messages

from .models import User, Course, Chapter, Video, Enrolled, Notes
from .forms import CourseForm


# Index view
def index(request):
	return render(request, "edYou/index.html", {
        "courses": Course.objects.order_by('-id').all()[:3]
    })


# Sign in view
def signin(request):

    # Redirect if user is already signed in
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))

    # Check request method
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get("username"), password=request.POST.get("password"))

        # Attempt to log user in
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        
        else:
            messages.add_message(request, messages.WARNING, 'Invalid username and/or password')
            return HttpResponseRedirect(reverse("signin"))

    else:
        return render(request, "edYou/signin.html")


# Sign out view
def signout(request):

    logout(request)
    return HttpResponseRedirect(reverse("index"))


# Sign up view
def signup(request):

    # Redirect if user is already signed in
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse("index"))
    
    # Check request method
    if request.method == "POST":
        
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm = request.POST.get("confirm")
        email  = request.POST.get("email")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")

        # Check if passwords match
        if password != confirm:
            return render(request, "edYou/signup.html", {
                "message": "Passwords must match"
            })
        
        # Password length must be at least 8
        elif len(password) < 8:
            return render(request, "edYou/signup.html", {
                "message": "Password must be at least 8 characters long"
            })
        
        # Attempt to create user
        try:
            user = User.objects.create_user(username, email, password, first_name=fname, last_name=lname)
            user.save()
        
        # Return message if username is unavailable
        except IntegrityError:
            return render(request, "edYou/signup.html", {
                "message": "Username already taken"
            })
        
        # Log user in
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

    else:
        return render(request, "edYou/signup.html")


# View to display all courses
def courses(request):

    # Pagination
    paginator = Paginator(Course.objects.order_by('-id').all(), 15)
    page = request.GET.get('page', 1)

    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        courses = paginator.page(1)
    except EmptyPage:
        courses = paginator.page(paginator.num_pages)
    
    return render(request, "edYou/courses.html", {
        "courses": courses
    })


# View to display a specific course
def course(request, id):
    
    # Check request method
    if request.method == 'POST':
        
        # User requests to enroll or unenroll
        if request.POST.get('enroll'):

            # Confirm user is signed in
            if request.user.is_authenticated:

                # Unenroll if user is enrolled
                if enrolled(request.user, id):
                    Enrolled.objects.get(user=request.user, course=Course.objects.get(id=id)).delete()

                # Enroll if user is not enrolled
                else:
                    enroll = Enrolled(user=request.user, course=Course.objects.get(id=id))
                    enroll.save()
                
                return HttpResponseRedirect(reverse('course', kwargs={
                    "id": id
                }))
            
            # Ask user to sign in if signed out
            else:
                messages.add_message(request, messages.INFO, 'Sign in to enroll to courses')
                return HttpResponseRedirect(reverse("signin"))
        
        # User requests to delete course
        elif request.POST.get('delete'):
            Course.objects.get(id=id).delete()
            return HttpResponseRedirect(reverse("index"))
        
        # User requests to edit course
        else:
            form = CourseForm(request.POST, request.FILES)
            if form.is_valid():
                course = Course(
                    id=id,
                    teacher=request.user,
                    name=form.cleaned_data['name'],
                    subject=form.cleaned_data['subject'],
                    language=form.cleaned_data['language'],
                    duration=form.cleaned_data['duration'],
                    difficulty=form.cleaned_data['difficulty'],
                    description=form.cleaned_data['description'],
                    img=request.FILES['img']
                )
                course.save()

                return HttpResponseRedirect(request.path)
    
    else:

        # Redirect user to enrolled course view if enrolled
        if enrolled(request.user, id):
            return HttpResponseRedirect(reverse("enrolled_course", kwargs={
                "id": id
            }))

        course = Course.objects.get(id=id)
        return render(request, "edYou/course.html", {
            "course": course,
            "chapters": Chapter.objects.filter(course=course),
            "form": CourseForm
        })


# View to return search results
def search(request):

    if request.GET.get("q"):
        name = list(Course.objects.filter(name__icontains=request.GET.get("q")))
        desc = list(Course.objects.filter(description__icontains=request.GET.get("q")))
        return render(request, "edYou/courses.html", {
            "courses": set(name + desc)
        })


# View to return filtered list of courses
def filter(request, param):

    # Return 404 if filter param is not valid
    choices = ['difficulty', 'duration', 'language', 'subject']
    if param.lower() not in choices:
        return render(request, "edYou/error.html", {
            "code": 404,
            "message": "Requested page not found"
        })

    # Return data if valid
    else:
        return render(request, "edYou/filter.html", {
            "unordered_courses": Course.objects.order_by(param.lower()).all(),
            "param": param.lower()
        })


# View to display user's dashboard
@login_required(login_url='/signin')
def dashboard(request):

    user_courses = Course.objects.filter(teacher=request.user)
    enrolled_courses = Course.objects.filter(id__in=Enrolled.objects.values('course').filter(user=request.user))

    return render(request, "edYou/dashboard.html", {
        "user_courses": user_courses,
        "enrolled_courses": enrolled_courses
    })


# View to create new course
@login_required(login_url='/signin')
def new_course(request):

    # Check request method
    if request.method == 'POST':

        # Create course if form is valid
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = Course(
                teacher=request.user,
                name=form.cleaned_data['name'],
                subject=form.cleaned_data['subject'],
                language=form.cleaned_data['language'],
                duration=form.cleaned_data['duration'],
                difficulty=form.cleaned_data['difficulty'],
                description=form.cleaned_data['description'],
                img=request.FILES['img']
            )
            course.save()

            return HttpResponseRedirect(reverse('course', kwargs={
                "id": course.id
            }))

    else:
        return render(request, "edYou/new_course.html", {'form': CourseForm()})


# View to display course for enrolled users
@login_required(login_url='/signin')
def enrolled_course(request, id):

    # Redirect user if user is not enrolled
    if not enrolled(request.user, id):
        return HttpResponseRedirect(reverse("course", kwargs={
            "id": id
        }))
    
    # User requests to save notes
    if request.method == 'POST':
        
        # Delete object if it's empty
        if request.POST.get('content') == '':
            try:
                Notes.objects.get(id=id).delete()
            except:
                pass
        
        # Save note contents
        else:
            try:
                notes = Notes.objects.get(user=request.user, course=Course.objects.get(id=id))
                notes.content = request.POST.get('content')
                notes.save()
            
            except ObjectDoesNotExist:
                notes = Notes.objects.get(user=request.user, course=Course.objects.get(id=id))
                notes.content = request.POST.get('content')
                notes.save()

        return HttpResponseRedirect(request.path + "?section=notes")

    else:
        
        # Get course and its chapters
        course = Course.objects.get(id=id)
        chapters = Chapter.objects.filter(course=course)

        # Get videos and append to its chapter
        for chapter in list(chapters):
            chapter.videos = Video.objects.filter(chapter=chapter)
        
        # Try to get user saved notes
        try:
            notes = Notes.objects.get(user=request.user, course=course)
        except:
            notes = None

        return render(request, "edYou/enrolled_course.html", {
            "course": course,
            "chapters": chapters,
            "notes": notes
        })


# View for users to edit their course chapters
def chapters(request, id):

    course = Course.objects.get(id=id)

    # Redirect if user is not course's owner
    if course.teacher != request.user:
        return HttpResponseRedirect(reverse("course", kwargs={
            "id": id
        }))
    
    # Check request method
    if request.method == 'POST':
        
        # User requests to create new chapter
        if request.POST.get('new-cname'):
            course = Course.objects.get(id=id)
            chapter = Chapter(course=course, name=request.POST.get('new-cname'))
            chapter.save()
        
        # User requests to edit chapter name
        elif request.POST.get('edit-cname'):
            chapter = Chapter.objects.get(id=request.POST.get('edit-cid'))
            
            # Validate user
            if chapter.course.teacher != request.user:
                return render(request, "edYou/error.html", {
                    "code": 403,
                    "message": "Unauthorised"
                })
            chapter.name = request.POST.get('edit-cname')
            chapter.save()

        # User requests to create new video
        elif request.POST.get('new-vname'):
            chapter = Chapter.objects.get(id=request.POST.get('new-cid'))
            
            # Validate user
            if chapter.course.teacher != request.user:
                return render(request, "edYou/error.html", {
                    "code": 403,
                    "message": "Unauthorised"
                })
            video = Video(chapter=chapter, name=request.POST.get('new-vname'), video=request.POST.get('new-vurl'))
            video.save()

        # User requests to edit video details
        elif request.POST.get('edit-vid'):
            video = Video.objects.get(id=request.POST.get('edit-vid'))
            
            # Validate user
            if video.chapter.course.teacher != request.user:
                return render(request, "edYou/error.html", {
                    "code": 403,
                    "message": "Unauthorised"
                })
            video.name = request.POST.get('edit-vname')
            video.video = request.POST.get('edit-vurl')
            video.save()
        
        # User requests to delete chapter
        elif request.POST.get('del-cid'):
            chapter = Chapter.objects.get(id=request.POST.get('del-cid'))
            
            # Validate user
            if chapter.course.teacher != request.user:
                return render(request, "edYou/error.html", {
                    "code": 403,
                    "message": "Unauthorised"
                })
            chapter.delete()

        # User requests to delete video
        elif request.POST.get('del-vid'):
            video = Video.objects.get(id=request.POST.get('del-vid'))
            
            # Validate user
            if video.chapter.course.teacher != request.user:
                return render(request, "edYou/error.html", {
                    "code": 403,
                    "message": "Unauthorised"
                })
            video.delete()

        return HttpResponseRedirect(request.path)

    else:
        
        # Get course chapters and videos
        chapters = Chapter.objects.filter(course=course)
        for chapter in list(chapters):
            chapter.videos = Video.objects.filter(chapter=chapter)
            
        return render(request, "edYou/chapters.html", {
            "course": course,
            "chapters": chapters
        })


# Function to check if user is enrolled
def enrolled(user, id):
    try:
        Enrolled.objects.get(user=user, course=Course.objects.get(id=id))
        return True
    except:
        return False
