# The code is a shell script that sets file access control lists (ACLs) for a specified user on a given directory and all its parent directories up to the root directory. This is done using the setfacl command, which modifies the ACLs of a file or directory.

# sudo ./give_permission.sh ~/shared_folder target_user

leaf=$1
usr=$2
branch="$leaf"
while branch="$(dirname "$branch")"
do
     setfacl -m u:"$usr":x "$branch"  ||  break
     if [ "$branch" = / ]
     then
         break
     fi
done
setfacl -R -m u:"$usr":rwx "$leaf"

# https://superuser.com/questions/781938/allow-user-to-traverse-path-to-given-directory

