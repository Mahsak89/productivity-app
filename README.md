# DRF for task to do app

---

[Link for Repository](https://github.com/Mahsak89/productivity-app)

[Link for API](https://productive-c40034b33280.herokuapp.com/)

Here is an API provided by DJANGO REST FRAMWORK, so that users can make a task to do app without accessing to the backend straightly.

## Features

---

### **_AUTHENTICATION_**

- users can easily:

  - Register
  - Login
  - Logout

### **_CRUD FOR PROFILES_**

- List
- Instantly create profilesafter a user is created(using signal)
- Retrieve
- Edit

### **_CRUD FOR TASKS_**

- List
- Create
- Delete
- Retrieve
- Edit

### **_CRUD FOR CATEGORIES_**

- List
- Create
- Delete
- Retrieve
- Edit

### **_CRUD FOR STATES_**

- List
- Create
- Delete
- Retrieve

### **_FILTERING_**

for post profile and category and also added a filtering for habits base on user and habit id

## Data Model

![Image](image/erd.png)

---

I decided to create 4 different app to build my task to do API other than the user which is created by default.
I UPdated  this drf and added 2 more modals as needed  (habits and habit_tracker) and i .fix the error of accepting sooner date in deadline than the start date.

## Testing

---

I have manually tested the project by doing the following 
  

- task:
  
there is no form to edit when the user fetch a profile id and not the owner

![Image](image/drf/profilestest/6.png)

can delete and edit if log in:

![Image](image/drf/profilestest/candeleteandeditiflogin.png)

 validate start date and deadline time picking:

![Image](image/drf/profilestest/17.png)


there is no form to creat if not log in

![Image](image/drf/profilestest/5.png)



- profile :
  
 is owner is false when not lot login:

![Image](image/drf/profilestest/20.png)

valid  profile pic

![Image](image/drf/profilestest/9.png)

  


  
not found the user :

![Image](image/drf/profilestest/404notfound.png)


users can update their own profile

![Image](image/drf/profilestest/8.png)



- categories:
  
it would not show the create form when not log in

![Image](image/drf/profilestest/3.png)

no change is allowed when not  log in:

![Image](image/drf/profilestest/4.png)




updated when login:

![Image](image/drf/profilestest/7.png)



when not login there is no editing form:

![Image](image/drf/profilestest/10.png)

- habit and habit tracker:
  
    habit list:
    ![Image](image/drf/profilestest/11.png)
    
    habit detailed list:

    ![Image](image/drf/profilestest/12.png)

    handeling wrong input period tracker:

    ![Image](image/drf/profilestest/13.png)

    loged in habitcompletation:

    ![Image](image/drf/profilestest/14.png)

    log out in habitcompletation detail list

    ![Image](image/drf/profilestest/15.png)

    log out in habitcompletation list:

    ![Image](image/drf/profilestest/16.png)
    
   
   
    


    








- Passed the code through a PEP8 linter and confirmed that there are no problems
- Tested my code with invalid and valid inputs: to check both errors and permissions
  - CRUDS AND Permissions like:( u can see alot of more manula pic test in image folder in the drf folder.)
    ![Image](image/isownerisalse.png)

### **_Validator Testing_**

- PEP8

  - No errors were returned from PEP8online.com
    ![Image](image/pep8.png)

  I also test my app automatically in test.py in each app folder(tasks,profile...)

## Deployment

---

This project was deployed using Code Institute's mock terminal for Heroku. Below are the steps I followed to be able to deploy the terminal to the website:

1. Create a new Heroku app on the Heroku website.
2. Set config vars

3. Link the Heroku app to the repository on GitHub.
4. Click on Deploy.

### Create Repository

For this I used Github.

- Go to your profile, and press on "Repositories".
- Press "New" (Big green button).
- There I chose to use a template from Code Institute to have everything I needed for this project.
- Named my project [productivity-app](https://github.com/Mahsak89/productivity-app).
- Then clicked on "Create repository".
- Onces created, I opened the repository and clicked on "COdeanywhere" to create a new workplace.

### Fork Repository on GitHub

A copy of the GitHub Repository can be made by forking the GitHub account. Changes can be made on this copy without affecting the origional repository.

- Log in to GitHub and locate the repository in question.
- Locate the Fork button which can be found in the top corner, right-hand side of the page, inline with the repository name.
- Click this button to create a copy of the origional repository in your GitHub Account.

### To Clone The Repository on GitHub

- Click on the code button which is underneath the main tab and rdepository name to the right.
- In the "Clone with HTTPS' section, click on the clipboard icon to copy the URL.
- Open Git Bash in your IDE of choice.
- Change the current working directory to where you wan the cloned directory to be made.
- Type git clone, and then paste the URL copied form GitHub.
- Press enter and the clone of your repository will be created.

## Credits

---

- Slack community for information and also the few that helped me with the issues what I got.
- [CodeInstitute](https://learn.codeinstitute.net/courses).
- [YouTube](https://www.youtube.com/results?search_query=python+battleship+game)
