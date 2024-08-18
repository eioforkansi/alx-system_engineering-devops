**Postmortem Report: ALX System Engineering & DevOps Project 0x17 Outage**

**Incident Summary**
At approximately 07:37 West African Time (WAT), following the release of the ALX System Engineering & DevOps project 0x17, an isolated Ubuntu 14.04 container running an Apache web server experienced an outage. GET requests to the server resulted in 500 Internal Server Errors, instead of returning the expected HTML file for a basic Holberton WordPress site.

**Debugging Process**
The issue was first identified by bug debugger Emeka Oforkansi at around 19:20 WAT, after being assigned to resolve it. The steps taken to troubleshoot and resolve the issue were as follows:

1. **Process Verification**: Checked running processes using `ps aux`. Confirmed that two `apache2` processes—one owned by `root` and the other by `www-data`—were running as expected.
  
2. **Content Directory Check**: Inspected the `/etc/apache2/sites-available` directory and verified that the web server was serving content from `/var/www/html/`.

3. **Strace on Apache Processes**: Ran `strace` on the PID of the root `apache2` process in one terminal, while curling the server in another. This initial attempt provided no useful information.

4. **Strace on www-data Process**: Repeated the `strace` on the PID of the `www-data` process. This time, the `strace` output revealed a `-1 ENOENT (No such file or directory)` error when attempting to access the file `/var/www/html/wp-includes/class-wp-locale.phpp`.

5. **File Inspection**: Inspected the files in the `/var/www/html/` directory one by one, using Vim pattern matching. The typo in the file extension `.phpp` was located in the `wp-settings.php` file on line 137: `require_once(ABSPATH . WPINC . '/class-wp-locale.php');`.

6. **Issue Resolution**: Corrected the typo by removing the trailing `p` from the file extension.

7. **Validation**: Tested the fix by curling the server again, and this time received a 200 OK response.

8. **Automation**: Created a Puppet manifest to automate the fix for any future occurrences of this issue.

**Root Cause**
The outage was caused by a typo in the WordPress `wp-settings.php` file, where the file `class-wp-locale.php` was incorrectly referenced as `class-wp-locale.phpp`. This caused a critical application error, leading to the 500 Internal Server Error.

**Resolution**
The typo was corrected, and the server returned to normal operation. A Puppet manifest was created to automate the fix for any future instances of this error.

**Prevention**
To avoid similar issues in the future, the following measures are recommended:

1. **Thorough Testing**: Ensure that the application is thoroughly tested before deployment. This error would have been detected and resolved during testing.

2. **Uptime Monitoring**: Implement an uptime-monitoring service like UptimeRobot to provide instant alerts in the event of a website outage.

3. **Automation**: The Puppet manifest `0-strace_is_your_friend.pp` has been created to automate the correction of any `.phpp` extensions in the `wp-settings.php` file.

