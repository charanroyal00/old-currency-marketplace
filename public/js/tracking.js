const API_BASE = "http://127.0.0.1:8000/api";

/* =========================================================
                    ORDER ID
========================================================= */

const params = new URLSearchParams(window.location.search);

const orderId = params.get("order");

const orderIdElement = document.getElementById("orderId");

const orderStatus = document.getElementById("orderStatus");

const deliveryDate = document.getElementById("deliveryDate");

const homeButton = document.getElementById("homeButton");

/* =========================================================
                    VALIDATE
========================================================= */

if (!orderId) {
  orderIdElement.textContent = "ORDER NOT FOUND";

  orderStatus.textContent = "INVALID";
}

/* =========================================================
                FETCH ORDER
========================================================= */

async function loadOrder() {
  try {
    const response = await fetch(`${API_BASE}/orders/${orderId}/`);

    if (!response.ok) {
      throw new Error("Order not found");
    }

    const order = await response.json();

    console.log("Order:", order);

    renderOrder(order);
  } catch (error) {
    console.error(error);

    orderStatus.textContent = "UNAVAILABLE";
  }
}

/* =========================================================
                RENDER ORDER
========================================================= */

function renderOrder(order) {
  orderIdElement.textContent = `#${order.id}`;

  const status = String(order.status || "PENDING").toUpperCase();

  orderStatus.textContent = status;

  updateTimeline(status);

  /*
        For now we calculate an estimated
        delivery date.

        Later this should come from Django.
    */

  const date = new Date();

  date.setDate(date.getDate() + 5);

  deliveryDate.textContent = date.toLocaleDateString("en-IN", {
    day: "numeric",
    month: "long",
    year: "numeric",
  });
}

/* =========================================================
                TIMELINE
========================================================= */

function updateTimeline(status) {
  const items = document.querySelectorAll(".timeline-item");

  let activeIndex = 0;

  switch (status) {
    case "PENDING":
    case "PLACED":
      activeIndex = 0;
      break;

    case "PAID":
    case "CONFIRMED":
      activeIndex = 1;
      break;

    case "PROCESSING":
      activeIndex = 2;
      break;

    case "SHIPPED":
      activeIndex = 3;
      break;

    case "DELIVERED":
      activeIndex = 4;
      break;

    default:
      activeIndex = 0;
  }

  items.forEach((item, index) => {
    if (index <= activeIndex) {
      item.classList.add("active");
    } else {
      item.classList.remove("active");
    }
  });
}

/* =========================================================
                    HOME
========================================================= */

homeButton.addEventListener("click", () => {
  window.location.href = "/";
});

/* =========================================================
                    ANIMATION
========================================================= */

gsap.from(".tracking-header > *", {
  opacity: 0,

  y: 30,

  stagger: 0.15,

  duration: 0.8,

  ease: "power3.out",
});

gsap.from(".tracking-card", {
  opacity: 0,

  y: 50,

  duration: 1,

  delay: 0.3,

  ease: "power3.out",
});

/* =========================================================
                    INITIALIZE
========================================================= */

if (orderId) {
  loadOrder();
}
