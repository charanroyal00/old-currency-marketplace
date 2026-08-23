/* ==========================================================
                    NUMIS AUTHENTICATION
========================================================== */

console.log("NUMIS AUTH JS LOADED");

const API_BASE = "http://127.0.0.1:8000/api";

let forgotEmail = "";

/* ==========================================================
                    DOM READY
========================================================== */

document.addEventListener("DOMContentLoaded", () => {
  /* ======================================================
                        ELEMENTS
    ====================================================== */

  const registerTab = document.getElementById("registerTab");
  const loginTab = document.getElementById("loginTab");

  const registerForm = document.getElementById("registerForm");
  const loginForm = document.getElementById("loginForm");
  const forgotForm = document.getElementById("forgotForm");
  const otpForm = document.getElementById("otpForm");
  const resetForm = document.getElementById("resetForm");

  const indicator = document.querySelector(".tab-indicator");

  const switchToLogin = document.getElementById("switchToLogin");
  const switchToRegister = document.getElementById("switchToRegister");

  const forgotBtn = document.getElementById("Forgot-Password");

  const backToLogin1 = document.getElementById("backToLogin1");
  const backToLogin2 = document.getElementById("backToLogin2");

  const forgotPasswordForm = document.getElementById("forgotPasswordForm");

  const coin = document.querySelector(".visual-coin");
  const orbitOne = document.querySelector(".orbit-one");
  const orbitTwo = document.querySelector(".orbit-two");

  const ambient = document.querySelectorAll(".ambient");

  /* ======================================================
                    INTRO ANIMATION
    ====================================================== */

  if (typeof gsap !== "undefined") {
    const introTimeline = gsap.timeline();

    introTimeline

      .from(".auth-visual", {
        x: -80,
        opacity: 0,
        duration: 1.2,
        ease: "power3.out",
      })

      .from(
        ".auth-panel",
        {
          x: 80,
          opacity: 0,
          duration: 1.2,
          ease: "power3.out",
        },
        "-=1",
      )

      .from(
        ".visual-coin",
        {
          scale: 0,
          rotationY: -180,
          opacity: 0,
          duration: 1.5,
          ease: "back.out(1.7)",
        },
        "-=0.7",
      )

      .from(
        ".visual-eyebrow,.visual-center h1,.visual-description",
        {
          y: 25,
          opacity: 0,
          stagger: 0.12,
          duration: 0.8,
          ease: "power3.out",
        },
        "-=0.8",
      )

      .from(
        ".auth-switcher,.form-heading,form,.form-footer",
        {
          y: 25,
          opacity: 0,
          stagger: 0.12,
          duration: 0.7,
          ease: "power3.out",
        },
        "-=0.7",
      );

    /* ==================================================
                    CONTINUOUS ANIMATIONS
        ================================================== */

    if (coin) {
      gsap.to(coin, {
        rotationY: "+=360",
        duration: 18,
        repeat: -1,
        ease: "none",
      });

      gsap.to(coin, {
        y: -12,
        duration: 3,
        repeat: -1,
        yoyo: true,
        ease: "sine.inOut",
      });
    }

    if (orbitOne) {
      gsap.to(orbitOne, {
        rotation: "+=360",
        duration: 25,
        repeat: -1,
        ease: "none",
      });
    }

    if (orbitTwo) {
      gsap.to(orbitTwo, {
        rotation: "-=360",
        duration: 32,
        repeat: -1,
        ease: "none",
      });
    }

    ambient.forEach((circle, index) => {
      gsap.to(circle, {
        x: index % 2 === 0 ? 50 : -50,

        y: index % 2 === 0 ? -30 : 30,

        duration: 6 + index,

        repeat: -1,

        yoyo: true,

        ease: "sine.inOut",
      });
    });
  }

  /* ======================================================
                    HIDE ALL FORMS
    ====================================================== */

  function hideAllForms() {
    if (registerForm) registerForm.classList.remove("active");

    if (loginForm) loginForm.classList.remove("active");

    if (forgotForm) forgotForm.classList.remove("active");

    if (otpForm) otpForm.classList.remove("active");

    if (resetForm) resetForm.classList.remove("active");
  }

  /* ======================================================
                    SHOW REGISTER
    ====================================================== */

  function showRegister() {
    hideAllForms();

    if (registerForm) registerForm.classList.add("active");

    if (registerTab) registerTab.classList.add("active");

    if (loginTab) loginTab.classList.remove("active");

    if (indicator && typeof gsap !== "undefined") {
      gsap.to(indicator, {
        x: 0,

        width: registerTab.offsetWidth,

        duration: 0.5,

        ease: "power3.out",
      });
    }

    if (registerForm && typeof gsap !== "undefined") {
      gsap.fromTo(
        registerForm,

        {
          opacity: 0,
          x: -25,
        },

        {
          opacity: 1,
          x: 0,
          duration: 0.5,
        },
      );
    }
  }

  /* ======================================================
                    SHOW LOGIN
    ====================================================== */

  function showLogin() {
    hideAllForms();

    if (loginForm) loginForm.classList.add("active");

    if (registerTab) registerTab.classList.remove("active");

    if (loginTab) loginTab.classList.add("active");

    if (indicator && typeof gsap !== "undefined") {
      gsap.to(indicator, {
        x: loginTab.offsetLeft,

        width: loginTab.offsetWidth,

        duration: 0.5,

        ease: "power3.out",
      });
    }

    if (loginForm && typeof gsap !== "undefined") {
      gsap.fromTo(
        loginForm,

        {
          opacity: 0,
          x: 25,
        },

        {
          opacity: 1,
          x: 0,
          duration: 0.5,
        },
      );
    }
  }

  /* ======================================================
                    SHOW FORGOT
    ====================================================== */

  function showForgot() {
    hideAllForms();

    if (forgotForm) forgotForm.classList.add("active");

    if (registerTab) registerTab.classList.remove("active");

    if (loginTab) loginTab.classList.add("active");

    if (forgotForm && typeof gsap !== "undefined") {
      gsap.fromTo(
        forgotForm,

        {
          opacity: 0,
          x: 30,
        },

        {
          opacity: 1,
          x: 0,
          duration: 0.5,
        },
      );
    }
  }

  /* ======================================================
                    SHOW OTP
    ====================================================== */

  function showOTP() {
    hideAllForms();

    if (otpForm) otpForm.classList.add("active");

    if (registerTab) registerTab.classList.remove("active");

    if (loginTab) loginTab.classList.add("active");

    if (otpForm && typeof gsap !== "undefined") {
      gsap.fromTo(
        otpForm,

        {
          opacity: 0,
          x: 30,
        },

        {
          opacity: 1,
          x: 0,
          duration: 0.5,
        },
      );
    }
  }

  /* ======================================================
                    SHOW RESET
    ====================================================== */

  function showReset() {
    hideAllForms();

    if (resetForm) resetForm.classList.add("active");

    if (resetForm && typeof gsap !== "undefined") {
      gsap.fromTo(
        resetForm,

        {
          opacity: 0,
          x: 30,
        },

        {
          opacity: 1,
          x: 0,
          duration: 0.5,
        },
      );
    }
  }

  /* ======================================================
                    TAB EVENTS
    ====================================================== */

  if (registerTab) registerTab.addEventListener("click", showRegister);

  if (loginTab) loginTab.addEventListener("click", showLogin);

  if (switchToLogin) switchToLogin.addEventListener("click", showLogin);

  if (switchToRegister)
    switchToRegister.addEventListener("click", showRegister);

  /* ======================================================
                    FORGOT BUTTON
    ====================================================== */

  if (forgotBtn) {
    forgotBtn.addEventListener("click", function (e) {
      e.preventDefault();

      showForgot();
    });
  }

  if (backToLogin1) {
    backToLogin1.addEventListener("click", function () {
      showLogin();
    });
  }

  if (backToLogin2) {
    backToLogin2.addEventListener("click", function () {
      showLogin();
    });
  }

  /* ======================================================
                    FORGOT PASSWORD
    ====================================================== */

  if (forgotPasswordForm) {
    forgotPasswordForm.addEventListener("submit", async (e) => {
      e.preventDefault();

      forgotEmail = document.getElementById("forgotEmail").value.trim();

      try {
        const response = await fetch(`${API_BASE}/forgot-password/`, {
          method: "POST",

          headers: {
            "Content-Type": "application/json",
          },

          body: JSON.stringify({
            email: forgotEmail,
          }),
        });

        const data = await response.json();

        if (response.ok) {
          alert("OTP Sent Successfully");

          showOTP();
        } else {
          alert(data.email?.[0] || data.message || "Unable to send OTP");
        }
      } catch (error) {
        console.error("FORGOT PASSWORD ERROR:", error);

        alert("Server Error");
      }
    });
  }

  /* ======================================================
                    INITIAL TAB
    ====================================================== */

  if (indicator && registerTab && typeof gsap !== "undefined") {
    gsap.set(indicator, {
      x: 0,

      width: registerTab.offsetWidth,
    });
  }
});

/* ==========================================================
                    REGISTER
========================================================== */

const registerFormElement = document.getElementById("registerFormElement");

if (registerFormElement) {
  registerFormElement.addEventListener("submit", async (e) => {
    e.preventDefault();

    const email = document.getElementById("registerEmail").value.trim();

    const username = document.getElementById("registerUsername").value.trim();

    const password = document.getElementById("registerPassword").value;

    const phone = document.getElementById("registerContact").value.trim();

    try {
      const response = await fetch(`${API_BASE}/register/`, {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({
          username: username,

          email: email,

          password: password,

          phone: phone,

          role: "customer",
        }),
      });

      const data = await response.json();

      if (response.ok) {
        console.log("REGISTRATION RESPONSE:", data);

        alert("Registration Successful!");

        registerFormElement.reset();

        const loginTab = document.getElementById("loginTab");

        if (loginTab) loginTab.click();
      } else {
        console.error("REGISTRATION ERROR:", data);

        alert(
          data.username?.[0] ||
            data.email?.[0] ||
            data.password?.[0] ||
            data.phone?.[0] ||
            "Registration Failed",
        );
      }
    } catch (error) {
      console.error("REGISTRATION REQUEST ERROR:", error);

      alert("Unable to connect to server.");
    }
  });
}

/* ==========================================================
                    LOGIN
========================================================== */

const loginFormElement = document.getElementById("loginFormElement");

if (loginFormElement) {
  loginFormElement.addEventListener("submit", async (e) => {
    e.preventDefault();

    console.log("LOGIN SUBMITTED");

    const username = document.getElementById("loginUsername").value.trim();

    const password = document.getElementById("loginPassword").value;

    if (!username || !password) {
      alert("Please enter your username and password.");

      return;
    }

    try {
      console.log("SENDING LOGIN REQUEST...");

      const response = await fetch(`${API_BASE}/login/`, {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({
          username: username,

          password: password,
        }),
      });

      console.log("LOGIN HTTP STATUS:", response.status);

      const data = await response.json();

      /* ==================================================
                    IMPORTANT JWT DEBUG
            ================================================== */

      console.log("==============================");

      console.log("LOGIN RESPONSE:", data);

      console.log("ACCESS TOKEN:", data.access);

      console.log("REFRESH TOKEN:", data.refresh);

      console.log("ACCESS TOKEN LENGTH:", data.access ? data.access.length : 0);

      console.log("==============================");

      /* ==================================================
                        LOGIN SUCCESS
            ================================================== */

      if (response.ok && data.access) {
        /* ----------------------------------------------
                        SAVE JWT
                ---------------------------------------------- */

        localStorage.setItem("access", data.access);

        localStorage.setItem("refresh", data.refresh);

        /* ----------------------------------------------
                        VERIFY STORAGE
                ---------------------------------------------- */

        console.log("JWT ACCESS TOKEN SAVED:");

        console.log(localStorage.getItem("access"));

        console.log("JWT REFRESH TOKEN SAVED:");

        console.log(localStorage.getItem("refresh"));

        alert("Login Successful!");

        /* ----------------------------------------------
                        REDIRECT
                ---------------------------------------------- */

        window.location.href = "../index.html";
      } else {
        console.error("LOGIN ERROR:", data);

        alert(
          data.username?.[0] ||
            data.detail ||
            data.non_field_errors?.[0] ||
            "Invalid username or password.",
        );
      }
    } catch (error) {
      console.error("LOGIN REQUEST ERROR:", error);

      alert("Unable to connect to server.");
    }
  });
}

/* ==========================================================
                    OTP VERIFY
========================================================== */

const otpVerifyForm = document.getElementById("otpVerifyForm");

if (otpVerifyForm) {
  otpVerifyForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const otp =
      document.getElementById("otp1").value +
      document.getElementById("otp2").value +
      document.getElementById("otp3").value +
      document.getElementById("otp4").value +
      document.getElementById("otp5").value +
      document.getElementById("otp6").value;

    try {
      const response = await fetch(`${API_BASE}/verify-otp/`, {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({
          email: forgotEmail,

          otp: otp,
        }),
      });

      const data = await response.json();

      if (response.ok) {
        alert("OTP Verified");

        showReset();
      } else {
        alert(data.detail || data.non_field_errors?.[0] || "Invalid OTP");
      }
    } catch (error) {
      console.error("OTP ERROR:", error);

      alert("Server Error");
    }
  });
}

/* ==========================================================
                    RESET PASSWORD
========================================================== */

const resetPasswordForm = document.getElementById("resetPasswordForm");

if (resetPasswordForm) {
  resetPasswordForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const newPassword = document.getElementById("newPassword").value;

    try {
      const response = await fetch(`${API_BASE}/reset-password/`, {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify({
          email: forgotEmail,

          new_password: newPassword,
        }),
      });

      const data = await response.json();

      if (response.ok) {
        alert("Password Reset Successful");

        const loginTab = document.getElementById("loginTab");

        if (loginTab) loginTab.click();
      } else {
        alert(data.detail || data.message || "Unable to reset password");
      }
    } catch (error) {
      console.error("RESET PASSWORD ERROR:", error);

      alert("Server Error");
    }
  });
}
