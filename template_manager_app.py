import streamlit as st
import os
import shutil
from pathlib import Path

def list_templates(category):
    template_dir = Path("templates/html_templates") / category
    if template_dir.exists():
        return [f.name for f in template_dir.glob("*.html")]
    return []

def read_template(category, template_name):
    template_path = Path("templates/html_templates") / category / template_name
    if template_path.exists():
        with open(template_path, "r", encoding="utf-8") as f:
            return f.read()
    return None

def save_template(category, template_name, content):
    template_dir = Path("templates/html_templates") / category
    template_dir.mkdir(parents=True, exist_ok=True)
    
    template_path = template_dir / template_name
    with open(template_path, "w", encoding="utf-8") as f:
        f.write(content)

def delete_template(category, template_name):
    template_path = Path("templates/html_templates") / category / template_name
    if template_path.exists():
        os.remove(template_path)

st.title("Email Template Manager")

# Template categories
categories = [
    "black_friday", "announcement", "blog_updates", "business",
    "deals_offers", "ecommerce", "events_invitations", "holiday",
    "notification", "survey_quizzes"
]

st.markdown("""
<style>
    .stSelectbox {
        margin-bottom: 1rem;
    }
    .template-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
        gap: 1rem;
        padding: 1rem;
    }
    .template-card {
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 1rem;
        background: white;
    }
    .template-actions {
        display: flex;
        gap: 0.5rem;
        margin-top: 1rem;
    }
    .iframe-container {
        border: 1px solid #e0e0e0;
        border-radius: 5px;
        padding: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

st.sidebar.title("Navigation")

# Sidebar for navigation
operation = st.sidebar.radio(
    "Select Operation",
    ["Browse Templates", "Add New Template", "Manage Templates"]
)

# Main content area
if operation == "Browse Templates":
    st.subheader("Browse Templates by Category")
    category = st.selectbox("Select Category", categories, key="category_select")

if operation == "Browse Templates":
    templates = list_templates(category)
    if templates:
        st.write(f"Found {len(templates)} templates in {category} category")
        
        for template_name in templates:
            template_content = read_template(category, template_name)
            if template_content:
                with st.container():
                    st.markdown("---")
                    st.subheader(template_name.replace(".html", "").replace("_", " ").title())
                    
                    # Preview and Code tabs
                    tab1, tab2 = st.tabs(["Preview", "HTML Code"])
                    
                    with tab1:
                        st.components.v1.html(template_content, height=500, scrolling=True)
                        
                        # Download button
                        st.download_button(
                            "Download Template",
                            template_content,
                            file_name=template_name,
                            mime="text/html"
                        )
                    
                    with tab2:
                        st.code(template_content, language="html", line_numbers=True)
                        
                        # Copy code button
                        if st.button("Copy Code", key=f"copy_{template_name}"):
                            st.write("Code copied to clipboard!")
                            
                    st.markdown("---")
    else:
        st.info(f"No templates found in {category} category")

elif operation == "Add New Template":
    st.header("Add New Template")
    
    # Create columns for form layout
    col1, col2 = st.columns([1, 2])
    
    with col1:
        category = st.selectbox("Select Category", categories)
        new_template_name = st.text_input("Template Name")
        
    with col2:
        template_content = st.text_area("HTML Content", height=400, placeholder="Paste your HTML template here...")
        
        if st.button("Save Template", type="primary"):
            if new_template_name and template_content:
                if not new_template_name.endswith(".html"):
                    new_template_name += ".html"
                save_template(category, new_template_name, template_content)
                st.success(f"✅ Template {new_template_name} saved successfully!")
                
                # Preview the saved template
                st.subheader("Preview")
                st.components.v1.html(template_content, height=500, scrolling=True)
            else:
                st.error("Please provide both template name and content")

elif operation == "Manage Templates":
    st.header("Manage Templates")
    
    # Create tabs for different operations
    tab1, tab2 = st.tabs(["Update Templates", "Delete Templates"])
    
    with tab1:
        category = st.selectbox("Select Category", categories, key="update_category")
        templates = list_templates(category)
        
        if templates:
            selected_template = st.selectbox("Select Template to Update", templates)
            
            if selected_template:
                current_content = read_template(category, selected_template)
                
                # Show current preview
                st.subheader("Current Version")
                st.components.v1.html(current_content, height=300, scrolling=True)
                
                # Edit area
                new_content = st.text_area("Edit HTML Content", value=current_content, height=400)
                
                col1, col2 = st.columns([1, 2])
                with col1:
                    if st.button("Update Template", type="primary"):
                        save_template(category, selected_template, new_content)
                        st.success(f"✅ Template {selected_template} updated successfully!")
                
                with col2:
                    if st.button("Preview Changes"):
                        st.subheader("Preview of Changes")
                        st.components.v1.html(new_content, height=300, scrolling=True)
        else:
            st.info(f"No templates found in {category} category")
    
    with tab2:
        category = st.selectbox("Select Category", categories, key="delete_category")
        templates = list_templates(category)
        
        if templates:
            selected_template = st.selectbox("Select Template to Delete", templates, key="delete_select")
            
            if selected_template:
                # Show preview of template to be deleted
                template_content = read_template(category, selected_template)
                st.components.v1.html(template_content, height=300, scrolling=True)
                
                if st.button("Delete Template", type="primary", key="delete_button"):
                    delete_template(category, selected_template)
                    st.success(f"✅ Template {selected_template} deleted successfully!")
                    st.experimental_rerun()
        else:
            st.info(f"No templates found in {category} category")
