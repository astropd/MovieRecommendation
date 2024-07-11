function switchLogin() {
    const login = document.getElementById("centerModalLogin");
    const signup = document.getElementById("centerModalSignup");

    login.classList.remove("hidden");
    signup.classList.add("hidden");
}

function switchSignup() {
    const login = document.getElementById("centerModalLogin");
    const signup = document.getElementById("centerModalSignup");

    login.classList.add("hidden");
    signup.classList.remove("hidden");
}