Datatable Execution
===================

tags: Data-table, execution

* In an empty directory initialize a project named "datatable_exec" with the current language

Simple Datatable Execution
--------------------------

* Create a specification "basic data table execution" with the following datatable 

     |id|name   |phone|
     |--|-------|-----|
     |1 |vishnu |999  |
     |2 |prateek|007  |
     |3 |nava   |100  |

* Create a scenario "datatable scenario" in specification "basic data table execution" with the following steps with implementation 

     |step text                |implementation|
     |-------------------------|--------------|
     |print <id> <name> <phone>|print params  |

* Execute the spec "basic data table execution" and ensure success
* Console should contain following lines in order 

     |console output                    |
     |----------------------------------|
     |param0=1,param1=vishnu,param2=999 |
     |param0=2,param1=prateek,param2=007|
     |param0=3,param1=nava,param2=100   |
