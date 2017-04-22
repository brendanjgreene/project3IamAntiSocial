# PROJECT FOR STREAM 3

You now have all the tools at your disposal to create a world class full stack membership site. Throughout Stream 3, we have been creating and assembling the key components of a site we have been calling We Are Social. The reason for this is that we would like to create a Social Entrepreneurship site that allows for the exchange of ideas that benefit both businesses and society as a whole.


## KEY COMPONENTS

The user stories (and components) involved in interacting with the site are as follows:

* A member registers to become part of the site community using an Accounts App
* Membership activated and maintained via recurring payments (payments may be used to fund projects) using an Accounts App (Stripe)
* Members can blog about their experiences, interests, and general ideas using a Blog App
* Members can engage in discussion about, and the potential progress of, projects and project categories of interest within the membership community using a Forum App
* Members can vote on whether a project will go ahead or not based on member voting using a Polls App


## USER EXPERIENCE

You have these key components already in place. Now use the skills you have learned across the three Streams to create a fantastic user experience for members and non-members alike.

This can include:

* Expanding or replacing the existing bootstrap theme to make the site an exciting and vibrant place to visit
* Adding Contact forms for potential members
* Adding About information, which might include maps of locations of the We Are Social globally located offices
* Social Media links

Use the knowledge learned from the Deployment lesson to deploy your project and show it off to the world!

# Deployed with sarcasm at:

https://i-am-anti-social.herokuapp.com

to update json run on command line:

- python manage.py dumpdata --natural-foreign -e contenttypes -e auth.Permission --indent=4 > db.json --settings=settings.dev

then update mySql with command line:

- heroku run python manage.py loaddata db.json --app i-am-anti-social
