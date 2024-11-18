## MICROSERVICE A: Asteroid Data
This microservice runs on Flask and employs the use of NASA's NEOWs (Near Earth Object Web Service) API. The user inputs a start and end date in the format YYYY-MM-DD and receives a JSON object that lists of all the asteroids, along with its specific data. Each asteroid is given a 'cartoon' asteroid icon. 

## TO RUN THE FILES
  1.Download the server.py and client.py files                                                                                                                                                    
  2.Install all the required dependencies (at the top of the files)                                                                                                                               
  3.Change the port accordingly                                                                                                                                                            
  4.Run the files in seperate terminals
  

  Queries to the API are sent in the form of 'https://api.nasa.gov/neo/rest/v1/feed?start_date=YYYY-MM-DD&end_date=YYYY-MM-DD&api_key=DEMO_KEY'                                                
      Example: https://api.nasa.gov/neo/rest/v1/feed?start_date=2024-11-03&end_date=2024-11-09&api_key=DEMO_KEY
  
  ## Parameters:
  start_date (YYYY-MM-DD)                                                                                                                                                                        
  end_date (YYYY-MM-DD) (optional, defaults to start_date if not entered)                                                                                                                        
  port number 

  ## REQUEST example:
  Request URL:                                                                                                                                                    <img width="503" alt="Screenshot 2024-11-17 at 5 02 34 PM" src="https://github.com/user-attachments/assets/72ddaaa0-3a62-4770-9f16-df97f8ee4a53">
                                             
  Request input:
  <img width="350" alt="Screenshot 2024-11-17 at 2 23 04 AM" src="https://github.com/user-attachments/assets/782eb2a0-a83c-4a12-bf7f-d201f5a24a81">


  If request fails, user is given the error 500:
  <img width="331" alt="Screenshot 2024-11-17 at 2 18 06 AM" src="https://github.com/user-attachments/assets/0e2e9aa3-22b0-4ba5-af6f-01a20636eedc">


  ## RECEIVE example:
  Receiving dates from the client side for the API:
  <img width="713" alt="Screenshot 2024-11-17 at 5 05 05 PM" src="https://github.com/user-attachments/assets/2c682c27-7a94-4e6a-84c5-71e39aa9ae9f">
  
   For succesful request:
  <img width="525" alt="Screenshot 2024-11-17 at 1 57 56 AM" src="https://github.com/user-attachments/assets/31c46211-3a2f-40dc-8ab7-f6981f88c618">

  For an unsuccessful request:
  <img width="768" alt="Screenshot 2024-11-17 at 2 15 07 AM" src="https://github.com/user-attachments/assets/1c08286d-e96c-4b0c-a5e1-ddfaa67a1d67">
    

    

 
