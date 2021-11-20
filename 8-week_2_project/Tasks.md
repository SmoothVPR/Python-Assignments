### Tasks
- [x] Use python libraries logging,csv (or) openpyxl,phonenumbers,numpy,pandas,datetime,sys

- [x] So we have FieldAgent files for NewYork Life Insurances.

- [x] Basically you need to sort the files in descending order of dates and 
      obtain the greatest dated file which is in the filenaming convention  
      20210219 here in the collection provided.

- [x] Check the file line count and measure that the file line count of the  
      latest file and the file line count of one level less decrement date  
      file has a variance of 500 lines.

- [x] If the line count difference is more than 500 lines reject the processing  
      of the file with exception message else process the latest file.

- [x] File if processed once should be stored in the reference file: 'NYL.lst'.  
      If in case we are reprocessing the same file once again should throw an  
      exception , saying already processed.

- [x] Now before reading the file capture the name of the file in NYL.lst file  
      so the filename is stored there for future reference.

- [x]  Replace the headers in the file c1 with c2 and c3 with c4 , just in case the file header is inconsistent:
    - c1='Agent Writing Contract Start Date (Carrier appointment start date)'
    - c2='Agent Writing Contract Start Date'
    - c3='Agent Writing Contract Status (actually active and cancelled\'s should come in two different files)'
    - c4='Agent Writing Contract Status'

- [x] Perform the following checks on the columns:
    - [x] The **phonenumbers** in the file should be US valid phone numbers in case they not Valid capture in the log file.
    - [x] Check if the State is a Valid US State
    - [x] Check is the Agent email is a valid email id

- [ ] Create a data frame of the headers as index and data as rows.Display the data frame.

- [ ] Create another Data Frame with which groups all the agents by Agency State.Display in the data frame.

- [ ] Create a Data Frame which gives the Agent Name , Agent Writing ContractStart Date , Date when an agent became A2O.

- [ ] Create a data visualization with the Data Frame using 9,10 use pandas built-in plot function for histogram.
