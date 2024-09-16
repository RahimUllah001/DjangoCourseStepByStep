# Building a Django Project with Integrated Root and Application Templates

## Project Overview

- This project is part of my ongoing Django Full Course, where I have implemented both concepts of placing templates inside the root directory and - inside the individual applications. This approach allows for flexibility and organization in managing templates. Root-level templates will be - - used for basic views such as home.html, while application-level templates will be restricted to templates specific to each application. - - -  - - Additionally, I have defined views in both the root directory and within each application to handle template rendering appropriately.
### Key Achievements:

1. **Project Structure:**
   - Created the following directory structure:
     - **Root Directory:** Contains a general `templates` folder for templates accessible across the project.
     - **Application-Level Templates:**
       - `course`: Contains its own `templates` folder with application-specific templates.
       - `fees`: Contains its own `templates` folder with application-specific templates.

2. **Template Setup:**
   - Defined templates inside two locations:
     - **Root Directory:** Accessible by the entire project.
     - **Application-Specific:** Each application (`course` and `fees`) has its own templates directory.

3. **Views:**
   - **Root View:**
     - Defined a root view in the `gs11` project to render `home.html` from the root directory's templates.
   - **Application-Specific Views:**
     - **`course` Application:** Defined views to handle application-specific templates within the `course` app.
     - **`fees` Application:** Defined views to handle application-specific templates within the `fees` app.


