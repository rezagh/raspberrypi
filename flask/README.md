$ mkdir myproject  
$ cd myproject  
$ python3 -m venv venv  
$ . venv/bin/activate
  
$ pip install flask, pymysql  
$ pip install --upgrade Flask  

if you want to access remotely add --host=0.0.0.0 to the run  

$ flask --app hello run --host=0.0.0.0  

now access the host locally via localhost:5000 or remotly using the host ip address