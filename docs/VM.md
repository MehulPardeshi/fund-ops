# Course server (VM)

The teaching team set up a Linux server for the course (Canvas announcement, Nov 11). We did not need it for Assignment 1, which ran in Colab. It will probably matter for Assignment 2 and the final project once the shared folders are filled.

## Log in once now and change your password

Everyone in the class got the same temporary password (it is in `OPAI_Student_Setup.pdf`, attached to the Canvas announcement). Until you change it, anyone in the class can log in as you.

1. Install **Cisco Secure Client** from [Software at CMU](https://www.cmu.edu/computing/software/titles/cisco-anyconnect-vpn-client/index.html) (free, macOS and Windows). Allow the system extension if your computer asks.
2. Open it, type `vpn.cmu.edu`, click **Connect**, sign in with your Andrew ID and approve Duo.
3. In Terminal (Mac) or PowerShell (Windows):
   ```
   ssh YOUR_ANDREW_ID@skings-f26.heinz.local.cmu.edu
   ```
   Enter the temporary password, enter it again when asked for the current password, then choose a new one. If it does not ask, run `passwd`.
4. Type `exit`. Disconnect the VPN when you are done.

Do not post passwords in the chat or in this repo.

## Folders

| Path | Who can open it |
|---|---|
| `/opt/94879/sections/B2/students/<your Andrew ID>` | You and the teaching team |
| `/opt/94879/sections/B2/teams/team02` | Our four members and the teaching team |
| `/opt/94879/SRC`, `/opt/94879/data`, `/opt/94879/model` | Everyone, read only (provided by the teaching team) |

Listing `/opt/94879` itself gives "Permission denied". That is expected; use the full paths.

## What the server has (checked Nov 12)

| | |
|---|---|
| CPU and memory | 6 cores, 30 GB, shared by the whole class |
| GPU | None. Colab's free GPU is faster for running models. |
| Disk | About 7 GB free for everyone. Do not store models or big datasets in your own folder. |
| Software | Python 3.14, PyTorch (CPU), numpy, pandas, git. No `transformers` yet. |
| Shared folders | Empty on Nov 12 |

## When to use it

- When an assignment or the teaching team tells us to, or puts code, data or models in the shared folders.
- To share files inside the team folder instead of sending them on WhatsApp.

You need the VPN only for this server. Colab, Drive, Canvas, Gmail and GitHub work without it.
