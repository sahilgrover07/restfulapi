## Restful API with Django Python to find leaderboard
<b>Dependencies</b>:

asgiref==3.3.4<br/>Django==3.2.2<br/>
djangorestframework==3.12.4<br/>
install==1.3.4<br/>
psycopg2==2.8.6<br/>
pytz==2021.1<br/>
sqlparse==0.4.1<br/>
typing-extensions==3.10.0.0

<h3>Steps to execute:</h3>
1. Git clone restfulapi</br>
git clone 


### Steps to Execute 
#### 1. Git clone restfulapi 
```bash
git clone https://github.com/sahilgrover07/restfulapi.git
```
#### 2. cd into restfulapi 
```bash
cd restfulapi
```
#### 3. Create virtual environment 
```bash
python -m venv virtualenv
```
#### 4. Activate virtual environment 
```bash
virtualenv\Scripts\activate
```
#### 5. Install dependencies
```bash
pip install requirements.txt
```
#### 6. Run the project 
```bash
python manage.py runserver
```
### Go to your postman<br/> 
<b>with get method</b> : <br/>
In order to fetch all the records sorted W.R.T. total score
<br/>
http://127.0.0.1:8000/getoradd/

![getalluser(sorted with the scores)](https://user-images.githubusercontent.com/55259770/117590845-55f1ef80-b0ff-11eb-87b4-841f36fef035.JPG)

<b>with post method</b> : <br/>
In order to put the record in DB.<br/>
It will automatically add the score to 0
<br/>
http://127.0.0.1:8000/getoradd/
![addingDetailToDB](https://user-images.githubusercontent.com/55259770/117591021-47580800-b100-11eb-95c6-3ef132461654.JPG)

<b> with get method </b> <br/>
In order to get praticular record from the DB<br/>
http://127.0.0.1:8000/userdetail/11/
![FetchingDetailsOfUserById](https://user-images.githubusercontent.com/55259770/117591509-d8c87980-b102-11eb-9acc-d328761e0826.JPG)

<b> with delete method </b> <br/>
In order to delete record from the DB<br/>
http://127.0.0.1:8000/del/12/

![DeleteUserById](https://user-images.githubusercontent.com/55259770/117591719-a79c7900-b103-11eb-8d60-f9ff72aa0045.JPG)

<b> with delete method </b> <br/>
In order to add score<br/>
<b>with post method</b> <br/>
http://127.0.0.1:8000/addorsub/11/
![addingScoreToDB](https://user-images.githubusercontent.com/55259770/117592131-73c25300-b105-11eb-9565-b7eca31d73d6.JPG)

In order to sub score<br/>
<b>with post method</b> <br/>
http://127.0.0.1:8000/addorsub/11/
![subtractingScoreFromDB](https://user-images.githubusercontent.com/55259770/117592162-a10f0100-b105-11eb-903e-5ed3682b68b3.JPG)






