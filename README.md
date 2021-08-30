# Simple_Flask_Api_MongoDB
1.pip install -r requirements.txt
2.python app.py

3.Добавить товар 
curl -X POST -H "Content-Type: application/json" \ --data "{"_id":1,"name":"Book","description":"go and buy","parameters" : [{"ram":100},{"PW":57}]}" \ http://127.0.0.1:5000/product_post 
4.curl localhost:5000/products - полуить список товар с фильтрацей по названию 
5.curl localhost:5000/products/pentium - полуить список товар с фильтрацей по параметру "pentium" 
6.curl localhost:5000/product/1 - получить описание товара по id 1
