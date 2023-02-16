"use strict"

const routine = document.querySelector("#routine")

routine.addEventListener("click", () => {
    const routine_id = routine.value 
    document.querySelector(`#${routine_id}`).hidden = false;
})