Tagged hooks spec level - Both AND and OR aggregation
=====================================================

tags: tagged_hooks, execution_hooks

* In an empty directory initialize a project named "tagged_hook_spec" without example spec
* Create a scenario "First scenario" in specification "First Spec" with the following steps with implementation 

     |step text                            |implementation                         |
     |-------------------------------------|---------------------------------------|
     |first spec first scenario first step |"first spec first scenario first step" |
     |first spec first scenario second step|"first spec first scenario second step"|

* Create a scenario "First scenario" in specification "Second Spec" with the following steps with implementation 

     |step text                             |implementation                          |
     |--------------------------------------|----------------------------------------|
     |second spec first scenario first step |"second spec first scenario first step" |
     |second spec first scenario second step|"second spec first scenario second step"|

* Create a scenario "First scenario" in specification "Third Spec" with the following steps with implementation 

     |step text                            |implementation                         |
     |-------------------------------------|---------------------------------------|
     |third spec first scenario first step |"third spec first scenario first step" |
     |third spec first scenario second step|"third spec first scenario second step"|

* Add tags "tag1,tag2,tag3" to specification "First Spec"
* Add tags "tag1,tag2" to specification "Second Spec"
* Add tags "tag1,tag4" to specification "Third Spec"

AND aggregation of hooks
------------------------

* Create "spec" level "before" hook with implementation "inside before spec hook" with "AND" aggregated tags 

     |tags|
     |----|
     |tag1|
     |tag2|

* Execute the current project and ensure success
* Console should contain following lines in order 

     |Console output                        |
     |--------------------------------------|
     |inside before spec hook               |
     |first spec first scenario first step  |
     |first spec first scenario second step |
     |inside before spec hook               |
     |second spec first scenario first step |
     |second spec first scenario second step|
     |third spec first scenario first step  |
     |third spec first scenario second step |

* Console should contain "inside before spec hook" "2" times

OR aggregation of hooks
-----------------------

* Create "spec" level "before" hook with implementation "inside before spec hook" with "OR" aggregated tags 

     |tags|
     |----|
     |tag3|
     |tag4|

* Create "spec" level "after" hook with implementation "inside after spec hook" with "OR" aggregated tags 

     |tags|
     |----|
     |tag3|

* Execute the current project and ensure success
* Console should contain following lines in order 

     |Console output                        |
     |--------------------------------------|
     |inside before spec hook               |
     |first spec first scenario first step  |
     |first spec first scenario second step |
     |inside after spec hook                |
     |second spec first scenario first step |
     |second spec first scenario second step|
     |inside before spec hook               |
     |third spec first scenario first step  |
     |third spec first scenario second step |

* Console should contain "inside before spec hook" "2" times
* Console should contain "inside after spec hook" "1" times
