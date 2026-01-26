In this project, I have created a lambda function that identifies EBS snapshots,
that are no longer associated to any active EC2 instance and deleted them empty storage and thus save costs.


First I created a lambda function(code for which is present in [test.py]) and provided it a role. 

Created and attached required policies to the role like:
- delete Snapshots
- describe Snapshots
- describe Volumes
- describe Instances





