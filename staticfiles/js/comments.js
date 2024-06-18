const editButtons = document.getElementsByClassName("btn-edit");
const commentText = document.getElementsById("content");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

//will try workaround //
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        let commentContent = document.getElementById(`comment${commentId}`).innerText;
        commentText.value = commentContent;
        submitButton.innerText = "Update";
        commentForm.setAttribute("action", `edit_comment/${commentId}`);
    });
} 

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let commentId = e.target.getAttribute("comment_id");
        deleteConfirm.href = `delete_comment/${commentId}`;
        deleteModal.show();
    });
}


/*
const editButtons = document.querySelectorAll(".btn-edit");
const deleteButtons = document.querySelectorAll(".btn-delete");
const commentForm = document.getElementById("commentForm");
const submitButton = document.getElementById("submitButton");
const deleteConfirm = document.getElementById("deleteConfirm");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));


editButtons.forEach(button => {
    button.addEventListener("click", (e) => {
        const commentId = e.target.getAttribute("comment_id");
        // Get the content of the specific comment
        const commentContent = document.querySelector(`#comment${commentId} .comment-content`).innerText.trim();
        
        
        const commentContentInput = commentForm.querySelector("textarea[name='content'], input[name='content']");
        if (commentContentInput) {
            commentContentInput.value = commentContent;
        }

        // Update the form action URL
        commentForm.setAttribute("action", `/edit_comment/${commentId}/`);
        submitButton.innerText = "Update";

        // Scroll to the form for better user experience
        commentForm.scrollIntoView({ behavior: "smooth" });
    });
});

// Handling the delete button click to show confirmation modal
deleteButtons.forEach(button => {
    button.addEventListener("click", (e) => {
        const commentId = e.target.getAttribute("comment_id");
        deleteConfirm.href = `/delete_comment/${commentId}/`;
        deleteModal.show();
    });
}); */