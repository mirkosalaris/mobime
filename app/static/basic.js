function react(event) {
    let value = $("#search-box input")[0].value;

    fillAvanzata(value);

    value = value.toLowerCase(); // to support case insensitive matching


    if (value.length > 0) {
        if ("hotel firenze".indexOf(value) === 0) {
            showHotel();
        } else if ("cinema firenze".indexOf(value) === 0) {
            showCinema();
        } else {
            hideEverything();
        }
    } else {
        hideEverything();
    }
}

function fillAvanzata(value) {
    // put the text of the search after "ricerca avanzata"
    $(".searchString").html(value)
}

function showHotel() {
    $("#search-result").show();
    $("#hotel").show();
     $("#cinema").hide();
}

function showCinema() {
    $("#search-result").show();
    $("#cinema").show();
     $("#hotel").hide();
}

function hideEverything() {
    $("#hotel").hide();
    $("#cinema").hide();
    $("#search-result").hide();
}


$("#search-box > form").keyup(react);
