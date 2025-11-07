from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector



app = FastAPI()

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "yashtech"
)
print("connected to mysql")




class Data(BaseModel):
    name:str
    age:int

data_list = []



@app.get("/")
def msg():
    return {"message":"i am more (Welcome to Yash Tech Industries)",
            "msg2":"server is running!"}


@app.get("/show/userid/{user_id}")
def data(user_id:int):
    return {"userid":user_id,
            "message":"id shown successfuly"}


@app.get("/more")
def more(user_name:str,user_address:str):
    return {"username":user_name,
            "useraddress":user_address}



@app.post("/send")
def good(data_coming:Data):
    my_cursor = mydb.cursor()
    row_query = "insert into users (name,age) values (%s,%s)"
    values = (data_coming.name, data_coming.age)
    show = my_cursor.execute(row_query,values)
    mydb.commit()
    return {"name":data_coming.name,
            "age":data_coming.age}




@app.get("/getdata")
def hell():
    my_cursor = mydb.cursor()
    my_cursor.execute("select * from users")
    result = my_cursor.fetchall()
    return {"data received":result}

