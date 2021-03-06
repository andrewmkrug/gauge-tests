Datatable row range execution
=============================

tags: Data-table, execution

* In an empty directory initialize a project named "datatable_row_exec" with the current language
* Create a specification "row range data table execution" with the following datatable 

     |id|name   |phone|
     |--|-------|-----|
     |1 |vishnu |999  |
     |2 |prateek|007  |
     |3 |nava   |100  |

Datatable execution with row number
-----------------------------------

* Create a scenario "datatable scenario" in specification "row range data table execution" with the following steps with implementation 

     |step text                |implementation|
     |-------------------------|--------------|
     |print <id> <name> <phone>|print params  |

* Execute the spec "row range data table execution" with row range "2" and ensure success
* Console should contain following lines in order 

     |console output                    |
     |----------------------------------|
     |param0=2,param1=prateek,param2=007|

* Console should not contain following lines 

     |console output                   |
     |---------------------------------|
     |param0=1,param1=vishnu,param2=999|
     |param0=3,param1=nava,param2=100  |

Datatable execution with row range
----------------------------------

* Create a scenario "datatable scenario" in specification "row range data table execution" with the following steps with implementation 

     |step text                |implementation|
     |-------------------------|--------------|
     |print <id> <name> <phone>|print params  |

* Execute the spec "row range data table execution" with row range "2-3" and ensure success
* Console should contain following lines in order 

     |console output                    |
     |----------------------------------|
     |param0=2,param1=prateek,param2=007|
     |param0=3,param1=nava,param2=100   |

* Console should not contain following lines 

     |console output                   |
     |---------------------------------|
     |param0=1,param1=vishnu,param2=999|
