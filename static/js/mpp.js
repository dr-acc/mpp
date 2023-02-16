// <!-- Made this bit of JS thinking I'll need it; or something like it, maybe a jinja version(?) to populate the drop-down list in the form with options; (i.e., to avoid a massive list of <option> tags) -->

        const selectBPM = document.getElementById("selectBPM");
        let bpms;
            for (let i = 20; i <= 200; i++) {
                bpmContents += "<option>" + i + "</option>";
            }

        selectBPM.innerHTML = bmps;

        // <select name="bpm" id="bmp"></select>


        const collapsible_buttons = document.getElementsByClassName("collapsible");
        let i;

        for (i=0; i < coll.length; i++) {
            collapsible_buttons[i].addEventListener("click", function() {
                this.classList.toggle("active");
                let content = this.nextElementSibling;
                if (content.style.display === "block")  {
                    content.style.display = "none";
                }  else    {
                    content.style.display="block";
                }
            });
        }
