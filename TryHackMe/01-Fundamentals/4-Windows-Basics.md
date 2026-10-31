# Windows Fundamentals

**Date Completed:** June 19, 2026  
**Category:** Operating Systems  
**Rooms Covered:** Windows Fundamentals 1

---

## Executive Summary

This document covers the basics of how the Windows Operating System works, including its file system, file permissions, user accounts, and built-in management tools. Understanding these basics is essential for a SOC role because most corporate computers run on Windows, making them a primary target for attacks.

---

## File System: NTFS vs. FAT

Modern versions of Windows use the **New Technology File System (NTFS)**.
Before NTFS, Windows used older systems like **FAT16/FAT32** and **HPFS**. Today, you still see FAT systems used in USB thumb drives and MicroSD cards, but not on main Windows laptops or enterprise servers.

### Why NTFS is better:

- **Journaling File System:** NTFS automatically tracks file changes in a hidden log file. If the computer crashes or loses power, it uses this log to automatically repair broken files and folders. FAT cannot do this.
- **Large File Support:** It supports individual files larger than 4GB.
- **Security:** It allows you to set specific permissions on folders and files.
- **Compression & Encryption:** It supports folder compression and native encryption using the Encrypting File System (EFS).

### Security Risk: Alternate Data Streams (ADS)

NTFS has a feature called Alternate Data Streams (ADS). Normally, every file has a main data stream (`$DATA`). ADS allows a file to hide extra, hidden streams of data inside itself.

- Windows File Explorer does not show these hidden streams to the user natively.
- **The Security Catch:** Hackers and malware writers often use ADS to hide malicious code inside normal-looking text files to trick users and simple security tools.

---

## Folder and File Permissions

Windows uses specific permissions to control what a user can or cannot do to a file or folder.

### The 6 Core Permissions:

1. **Full Control:** Can do absolutely anything, including changing permissions for others.
2. **Modify:** Can read, write, and delete the file/folder.
3. **Read & Execute:** Can view the file and run it if it is a program or script.
4. **List Folder Contents:** Can see the names of files inside a folder.
5. **Read:** Can open and look at the contents of the file.
6. **Write:** Can edit or add new data to the file.

---

## System Directories & Environment Variables

Windows uses **Environment Variables** to store basic system information, like the operating system path and the location of temporary files.

- **`%windir%`**: This is the shortcut variable for the main Windows directory (usually `C:\Windows`).
- **The `System32` Folder (`C:\Windows\System32`):** This folder contains critical files and tools that keep Windows running.

---

## Users, Groups, and the Principle of Least Privilege

Windows organizes users into **Groups** (like the _Users_ group or the _Administrators_ group) to manage permissions easily.

- **Inheritance:** When an administrator adds a user to a group, that user automatically inherits all the permissions of that group. A single user can belong to multiple groups at the same time.
- **The Principle of Least Privilege:** Users should default to a standard user account for daily tasks like browsing the web or writing documents. Running as an Administrator all the time is a huge security risk. If you accidentally click a malicious link while logged in as an admin, the malware will instantly gain full administrative power over your entire computer.

---

## Monitoring & Management Tools

Windows separates simple settings from advanced configurations using different menus:

### 1. Settings App vs. Control Panel

- **Settings:** The modern, simple menu for everyday adjustments.
- **Control Panel:** The classic menu where you access complex settings and perform advanced administrative actions. Sometimes, clicking an option in Settings will send you straight to the Control Panel.

### 2. Task Manager

The Task Manager gives you real-time visibility into what is happening on the machine right now:

- **Processes:** Shows all applications and background tasks currently running.
- **Performance:** Displays how much CPU and RAM (memory) the system is currently utilizing.

---

## Strategic Takeaway for a SOC Role

Understanding how Windows handles user groups and file systems helps an analyst spot weird behavior. For example, if a standard corporate user suddenly tries to edit files inside the `System32` folder, or uses PowerShell to look for hidden `Alternate Data Streams (ADS)`, it is a major red flag that an attack might be happening.
