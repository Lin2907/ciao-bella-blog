document.addEventListener("DOMContentLoaded", () => {
    const editButtons = document.querySelectorAll(".btn-edit");
    const deleteButtons = document.querySelectorAll(".btn-delete");
    const commentForm = document.getElementById("commentForm");
    const submitButton = document.getElementById("submitButton");
    const deleteConfirm = document.getElementById("deleteConfirm");
    const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));

    editButtons.forEach(button => {
        button.addEventListener("click", (e) => {
            const commentId = e.target.getAttribute("comment_id");
            const postSlug = document.querySelector("meta[name='post-slug']").getAttribute("content"); // Retrieve post slug from meta tag

            // Get the content of the specific comment
            const commentContent = document.querySelector(`#comment${commentId} .comment-content`).innerText.trim();
            const commentContentInput = commentForm.querySelector("textarea[name='content'], input[name='content']");
            if (commentContentInput) {
                commentContentInput.value = commentContent;
            }

            // Update the form action URL
            commentForm.setAttribute("action", `/post/${postSlug}/comment_edit/${commentId}/`);
            submitButton.innerText = "Update";

            // Scroll to the form for better user experience
            commentForm.scrollIntoView({ behavior: "smooth" });
        });
    });

    deleteButtons.forEach(button => {
        button.addEventListener("click", (e) => {
            const commentId = e.target.getAttribute("comment_id");
            const postSlug = document.querySelector("meta[name='post-slug']").getAttribute("content"); // Retrieve post slug from meta tag

            // Update the delete confirm URL
            deleteConfirm.href = `/post/${postSlug}/delete_comment/${commentId}/`;
            deleteModal.show();
        });
    });
});
