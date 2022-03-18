# addressbook

Here, I have created simple Address book to store and retrive the adderess data of addresses.
1. Keep your terminal inside "addressbook" directory
    

2. Create virtual environment 
   - virtualenv -p python3 env

   - source env/bin/activate

3. Install all required packages/libraries
   - pip install -r requirements.txt

4. Start FastApi uvicorn server (I have created main.py file inside the address dictionary)
   - uvicorn address.main:app --reload


-> Now on http://localhost:8000/docs you will be able to see the swager for all api's

-> There are major app
    -address
    -user

-> Project include CRUD operation for the address app,

-> To retrieve the addresses that are within a given distance and location coordinates we can call "address/get-nearby-addresses" GET api
    (Note: "distance" parameter is considered in Kilometers, e.g : 50 stands for 50 kilometers)
