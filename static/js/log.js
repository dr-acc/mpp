"use strict"

const routine = document.querySelector("#select_routine")

routine.addEventListener("change", () => {
    const routine_id = routine.value 
    document.querySelector(`#routine-${routine_id}`).hidden = false;
})



