import streamlit as st
from app.scraper import fetch_aws_blogs, fetch_blog_content
from app.summarizer import summarize_blog

# Streamlit App Title
st.set_page_config(page_title="AWS Blog Summarizer", layout="wide")
st.title("📚 AWS Blog Summarizer")

# Fetch AWS Blog List
st.sidebar.header("🔍 Select a Blog")
blogs = fetch_aws_blogs()

if not blogs:
    st.error("❌ Failed to fetch blogs. Please check the scraper.")
    st.stop()

# Blog Selection
blog_titles = [b["title"] for b in blogs]
selected_blog = st.sidebar.selectbox("Choose a blog to summarize:", blog_titles)

# Find Blog URL
blog_url = next((b["link"] for b in blogs if b["title"] == selected_blog), None)

if st.sidebar.button("Summarize Blog"):
    if not blog_url:
        st.error("❌ Blog URL not found.")
    else:
        with st.spinner(f"Fetching content from: {blog_url} ..."):
            blog_content = fetch_blog_content(blog_url)

        if not blog_content or "error" in blog_content.lower():
            st.error("⚠️ Failed to retrieve blog content. The page may have restricted access.")
        else:
            with st.spinner("Generating summary..."):
                summary = summarize_blog(blog_content)

            if isinstance(summary, dict) and "error" not in summary:
                with st.expander("🔍 **View Blog Summary**", expanded=True):
                    st.markdown(f"### 📝 **{selected_blog}**")
                    st.markdown(f"🔗 [Read Full Blog]({blog_url})")

                    st.markdown("**💡 Main Topic:**")
                    st.write(summary.get("main_topic", "Not Available"))

                    st.markdown("**⚡ Key Challenges:**")
                    for challenge in summary.get("challenges", []):
                        st.write(f"- {challenge}")

                    st.markdown("**🛠 Steps & Solutions:**")
                    for idx, step in enumerate(summary.get("solutions", []), start=1):
                        st.write(f"{idx}. {step}")

                    st.markdown("**🧰 AWS Services Used:**")
                    for service in summary.get("services_used", []):
                        st.write(f"- {service}")

                    st.markdown("**📌 Best Practices & Recommendations:**")
                    for practice in summary.get("best_practices", []):
                        st.write(f"- {practice}")

            else:
                st.error("⚠️ Failed to generate summary. The model may have returned an invalid response.")

# Sidebar Footer
st.sidebar.markdown("---")
st.sidebar.caption("📌 Developed by Navnit Shukla")