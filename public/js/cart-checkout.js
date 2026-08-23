gsap.registerPlugin(ScrollTrigger);

console.log("NUMIS Secure Checkout initialized.");

const API_BASE = "/api";

let cart = JSON.parse(localStorage.getItem("cart")) || [];

/* =========================================================
   ELEMENTS
========================================================= */

const checkoutItems = document.getElementById("checkoutItems");

const subtotalElement = document.getElementById("subtotal");

const shippingElement = document.getElementById("shippingCost");

const grandTotalElement = document.getElementById("grandTotal");

const paymentBtn = document.getElementById("paymentBtn");

/* =========================================================
   FORMAT PRICE
========================================================= */

function formatPrice(price) {
  return "₹" + Number(price || 0).toLocaleString("en-IN");
}

/* =========================================================
   SHIPPING
========================================================= */

function getShippingCost() {
  const selected = document.querySelector('input[name="delivery"]:checked');

  if (!selected) {
    return 0;
  }

  switch (selected.value) {
    case "express":
      return 499;

    case "priority":
      return 999;

    default:
      return 0;
  }
}

/* =========================================================
   CART TOTAL
========================================================= */

function calculateSubtotal() {
  return cart.reduce((total, item) => {
    const price = Number(item.price || 0);

    const quantity = Number(item.quantity || 1);

    return total + price * quantity;
  }, 0);
}

/* =========================================================
   RENDER CHECKOUT
========================================================= */

function renderCheckout() {
  checkoutItems.innerHTML = "";

  if (!cart.length) {
    checkoutItems.innerHTML = `
            <div class="empty-checkout">
                <h3>Your collection is empty.</h3>
                <a href="products.html">
                    Continue Shopping
                </a>
            </div>
        `;

    subtotalElement.textContent = "₹0";
    shippingElement.textContent = "Free";
    grandTotalElement.textContent = "₹0";

    paymentBtn.disabled = true;

    return;
  }

  paymentBtn.disabled = false;

  cart.forEach((product) => {
    const name = product.name || product.title || "Unnamed Product";

    const price = Number(product.price || 0);

    const quantity = Number(product.quantity || 1);

    const image = product.image || "https://placehold.co/150x150";

    const item = document.createElement("div");

    item.className = "checkout-item";

    item.innerHTML = `
            <div class="checkout-item-image">
                <img
                    src="${image}"
                    alt="${name}"
                >
            </div>

            <div class="checkout-item-info">

                <h3>${name}</h3>

                <p>
                    Quantity: ${quantity}
                </p>

                <strong>
                    ${formatPrice(price * quantity)}
                </strong>

            </div>
        `;

    checkoutItems.appendChild(item);
  });

  updateTotals();
}

/* =========================================================
   UPDATE TOTALS
========================================================= */

function updateTotals() {
  const subTotal = calculateSubtotal();

  const shipping = getShippingCost();

  const grandTotal = subTotal + shipping;

  subtotalElement.textContent = formatPrice(subTotal);

  shippingElement.textContent = shipping === 0 ? "Free" : formatPrice(shipping);

  grandTotalElement.textContent = formatPrice(grandTotal);
}

/* =========================================================
   DELIVERY EVENTS
========================================================= */

document.querySelectorAll('input[name="delivery"]').forEach((radio) => {
  radio.addEventListener("change", updateTotals);
});

/* =========================================================
   CUSTOMER DETAILS
========================================================= */

function getCustomerDetails() {

    const selectors = {
        fullName: "#checkoutFullName",
        email: "#checkoutEmail",
        phone: "#checkoutPhone",
        altPhone: "#checkoutAltPhone",
        address: "#checkoutAddress",
        city: "#checkoutCity",
        state: "#checkoutState",
        zip: "#checkoutZip",
        country: "#checkoutCountry"
    };

    const elements = {};

    for (const [key, selector] of Object.entries(selectors)) {
        elements[key] = document.querySelector(selector);

        if (!elements[key]) {
            console.error(
                `Checkout element not found: ${selector}`
            );

            throw new Error(
                `Checkout field is missing: ${selector}`
            );
        }
    }

    return {
        fullName: elements.fullName.value.trim(),
        email: elements.email.value.trim(),
        phone: elements.phone.value.trim(),
        altPhone: elements.altPhone.value.trim(),
        address: elements.address.value.trim(),
        city: elements.city.value.trim(),
        state: elements.state.value.trim(),
        zip: elements.zip.value.trim(),
        country: elements.country.value
    };
}

function validateCustomer(details) {

    if (!details.fullName) {
        alert("Please enter your full name.");
        return false;
    }

    if (!details.email) {
        alert("Please enter your email.");
        return false;
    }

    if (!details.phone) {
        alert("Please enter your WhatsApp number.");
        return false;
    }

    if (!details.address) {
        alert("Please enter your address.");
        return false;
    }

    if (!details.city) {
        alert("Please enter your city.");
        return false;
    }

    if (!details.state) {
        alert("Please enter your state.");
        return false;
    }

    if (!/^\d{6}$/.test(details.zip)) {
        alert("Please enter a valid 6-digit PIN code.");
        return false;
    }

    return true;
}

/* =========================================================
   SUBMIT CHECKOUT
========================================================= */

async function submitCheckout() {
  if (!cart.length) {
    alert("Your cart is empty.");

    return;
  }

  const customer = getCustomerDetails();

  if (!validateCustomer(customer)) {
    return;
  }

  const subtotal = calculateSubtotal();

  const shipping = getShippingCost();

  const grandTotal = subtotal + shipping;

  const payload = {
    customer: customer,

    cart: cart,

    subtotal: subtotal,

    shipping: shipping,

    grand_total: grandTotal,
  };

  console.log("Checkout payload:", payload);

  paymentBtn.disabled = true;

  paymentBtn.textContent = "Processing Order...";

  try {
    const response = await fetch(`${API_BASE}/checkout/submit/`, {
      method: "POST",

      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify(payload),
    });

    const contentType = response.headers.get("content-type") || "";

let data;

if (contentType.includes("application/json")) {
  data = await response.json();
} else {
  const text = await response.text();

  console.error("Non-JSON server response:", text);

  throw new Error(
    `Server returned ${response.status} instead of JSON.`
  );
}

if (!response.ok) {

  console.error("Checkout error:", data);

  throw new Error(
    data.detail ||
    data.message ||
    "Unable to place order."
  );
}

    console.log("Checkout successful:", data);

    localStorage.removeItem("cart");

    alert(`Order ${data.order_reference} created successfully!`);

    window.location.href = `payment.html?order=${encodeURIComponent(
    data.order_reference
)}`;
  } catch (error) {
    console.error("Checkout failed:", error);

    alert(error.message || "Unable to process checkout.");

    paymentBtn.disabled = false;

    paymentBtn.textContent = "Proceed to Secure Payment";
  }
}

/* =========================================================
   PAYMENT BUTTON
========================================================= */

if (paymentBtn) {
  paymentBtn.addEventListener("click", submitCheckout);
}

/* =========================================================
   INITIALIZE
========================================================= */

renderCheckout();

/* =========================================================
   GSAP
========================================================= */

gsap.from(".checkout-card", {
  opacity: 0,

  y: 40,

  duration: 0.8,

  stagger: 0.12,

  ease: "power3.out",
});

gsap.from(".checkout-summary", {
  opacity: 0,

  x: 50,

  duration: 0.9,

  ease: "power3.out",
});

console.log("Checkout cart loaded:", cart);
