    function setActiveNav(id) {
        // disable all navs, then (re)enable nav w/ $id
        $("#grumpy .navbar-nav").find("a.active").removeClass("active");
        $("#grumpy .navbar-nav " + id).find("a").addClass("active");
    };