***My first Postmortem***


Issue Summary:

Duration:

- Start Time: January 21, 2024, 10:30 AM WAT

- End Time: January 21, 2024, 11:15 AM WAT

Impact:

The Nginx server was completely unavailable during the incident.
Users experienced service downtime, leading to a disruption in accessing web applications.
Approximately 15% of the user base was affected.

Root Cause:

The root cause was identified as misconfiguration in the Nginx server settings, preventing it from starting correctly.

Timeline:

- 10:30 AM WAT:

Issue detected by monitoring tools, reporting Nginx server failure.

- 10:35 AM WAT:

Initial investigation started by checking Nginx error logs for any recent issues.

- 10:40 AM WAT:

Error logs showed a misconfiguration in the Nginx configuration file.
Investigation focused on recent changes to the configuration.

- 10:50 AM WAT:

Assumption made: Recent configuration changes might have syntax errors.
Configuration files were manually inspected and syntax was validated.

- 11:00 AM WAT:

Misleading path: Configuration syntax was correct. Attention shifted to server resource exhaustion.
System resources checked, and false positive assumption delayed the resolution.

- 11:10 AM WAT:

Issue escalated to senior system administrators for a more in-depth analysis.

- 11:15 AM WAT:

Root cause identified: Misconfiguration in the Nginx server block, causing a conflict in the virtual host settings.

- 11:20 AM WAT:

Resolution: 

Corrected the misconfiguration in the Nginx server block and restarted the Nginx service.
Root Cause and Resolution:

Root Cause:

The root cause was a misconfiguration in the Nginx server block. This prevented the Nginx server from starting successfully.

Resolution:

The immediate fix involved correcting the misconfiguration in the Nginx server block.
Long-term solution: Implemented a process to automate configuration file checks before restarting the Nginx service to catch syntax errors early.
Corrective and Preventative Measures:

Improvements/Fixes:

- Strengthen the deployment process to ensure configuration changes are thoroughly reviewed.

- Enhance monitoring for Nginx server health, with specific alerts for configuration-related issues.

Tasks:

 - Conduct a knowledge-sharing session to disseminate lessons learned from this incident.
 - Document best practices for Nginx configuration management.
 - Review and update incident response procedures for Nginx-related issues.
 - Schedule regular audits of Nginx configuration files to identify and rectify potential misconfigurations.
