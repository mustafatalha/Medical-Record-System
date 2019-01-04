# Medical-Record-System
## Multiple User Types Medical Record System with Django

### This web application meets with following requirements:

> The project will involve a database of medical records accessible by doctor(s), patient, nurse(s), and relatives.

> The records shall be created by the doctors (fictitious records, all 256 characters long, including the name (first and last), birth date and the diagnostics for the patient)

> The data base will have a password‐controlled access control system:
- All doctors will have access using user defined user‐name and password, of course the administration should verify that they are really doctors. 
- The patients will be issued a username as first letter of name + last‐name, initial authorization will be issued by the doctor. A scheme should be devised for conflicting user names. The password should be randomly generated by the system. 
- Nurses will be issued passwords similar to the patients. 
- The relatives will be defined to the system by the patients. 
- The passwords should be stored using SHA‐256 hashing.

> Accessing the records will be as follows:
- Doctors will have access to all the records of all patients, but authorization will be given by the patients.
- Patients will only access to their own records.
- Relatives may only access to records defined by the patients.
- Nurses will be authorized by the doctors, they can only access to records for which the doctor has the authority.

> The software should have a different user interface for users and admin.