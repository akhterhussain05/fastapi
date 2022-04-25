const selectionArea = document.querySelector("#select-area"),
fileinput = document.querySelector(".file-input");

let preview = document.getElementById("file-preview");
let removeimg = document.getElementById("remove-img");





removeimg.addEventListener("click",()=>{
    fileinput.value = null;
    preview.src=null;
    preview.style.display="none"
    removeimg.style.display="none"
    selectionArea.style.display=null
})

selectionArea.addEventListener("click",() => {
    fileinput.click()

});

fileinput.onchange=({
    target
}) =>{
    let file = target.files[0];
    if(file.type == "image/jpeg"){
        let image_url = URL.createObjectURL(file);
        preview.src = image_url
        selectionArea.style.display="none"
        removeimg.style.display=null
        preview.style.display=null
    }else{
        alert("please select a jpg file")
        finalinput.value = null
        
    }
}

