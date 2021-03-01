# About:
edYou, short for Educate Yourself is a web app which can serve as an online platform for free education. Similar to that of Udemy or Skillshare but only there is no money involved. So the teachers can provide online courses on any topic, and students have access to those courses for free. Even though instructors can provide free education through other online video sharing platforms, it can be very distracting to watch anything productive in websites like YouTube and in this website, people don't have to worry about distractions. You can either create your own course and manage it's chapters and videos, or you can enroll in any course available and learn completely online as the users are also allowed to save their notes on the database. 

The website's feautures include Video Sharing, File Upload, User Authentication and many more! The back-end uses 7 models and the front-end uses some JavaScript code to improve the UI. A lot of Bootstrap's features such as carousel, collapse and utilities have been used in the front-end. Several other back-end features such as File Upload, Django Forms and Custom Template Tags have also been used in this web app. 

The Web App has been configured for deployement on Heroku using a PostgreSQL database and uses environment variables to store deployment information for security and flexibility. It has also been configured to upload static and media files to an AWS S3 Bucket and serve it using Amazon CloudFront CDN sevice. The web app has been altered in a way in which it can be run both locally and on production.

# Running the application:
	-pip install -r requirements.txt
	-python3 manage.py runserver
