const API_BASE = "http://127.0.0.1:8000/api";

console.log("NUMIS PAYMENT LOADED");

const params = new URLSearchParams(window.location.search);

const orderId = params.get("order");

const orderItems = document.getElementById("orderItems");
const subtotalElement = document.getElementById("subtotal");
const shippingElement = document.getElementById("shipping");
const grandTotalElement = document.getElementById("grandTotal");
const payAmount = document.getElementById("payAmount");
const payButton = document.getElementById("payButton");

let order = null;

/* =========================================
        LOAD ORDER
========================================= */

async function loadOrder() {
  if (!orderId) {
    alert("Invalid order.");

    window.location.href = "/cart.html";

    return;
  }

  try {
    const response = await fetch(`${API_BASE}/orders/${orderId}/`);

    if (!response.ok) {
      throw new Error("Unable to load order.");
    }

    order = await response.json();

    console.log("ORDER:", order);

    renderOrder();
  } catch (error) {
    console.error(error);

    orderItems.innerHTML = "<p>Unable to load order.</p>";
  }
}

/* =========================================
        RENDER ORDER
========================================= */

function renderOrder() {
  /*
        Adjust these property names if your
        Django serializer uses different names.
    */

  const items = order.items || order.order_items || [];

  orderItems.innerHTML = "";

  items.forEach((item) => {
    const product = item.product_details || item.product || item;

    const name = product.name || item.product_name || "Collectible";

    const quantity = item.quantity || 1;

    const price = Number(item.price || product.price || 0);

    orderItems.innerHTML += `

            <div class="order-item">

                <div>

                    <h3>
                        ${name}
                    </h3>

                    <p>
                        Quantity: ${quantity}
                    </p>

                </div>

                <strong>
                    ₹${(price * quantity).toLocaleString("en-IN")}
                </strong>

            </div>

        `;
  });

  const subtotal = Number(order.subtotal || order.total || 0);

  const shipping = Number(order.shipping || order.shipping_cost || 0);

  const total = Number(order.total || subtotal + shipping);

  subtotalElement.textContent = `₹${subtotal.toLocaleString("en-IN")}`;

  shippingElement.textContent =
    shipping === 0 ? "Free" : `₹${shipping.toLocaleString("en-IN")}`;

  grandTotalElement.textContent = `₹${total.toLocaleString("en-IN")}`;

  payAmount.textContent = total.toLocaleString("en-IN");
}

/* =========================================
        PAYMENT METHOD
========================================= */

const paymentOptions = document.querySelectorAll('input[name="paymentMethod"]');

const upiPanel = document.getElementById("upiPanel");

const cardPanel = document.getElementById("cardPanel");

const codPanel = document.getElementById("codPanel");

paymentOptions.forEach((option) => {
  option.addEventListener("change", () => {
    document
      .querySelectorAll(".payment-option")
      .forEach((card) => card.classList.remove("active"));

    option.closest(".payment-option").classList.add("active");

    upiPanel.classList.add("hidden");
    cardPanel.classList.add("hidden");
    codPanel.classList.add("hidden");

    if (option.value === "upi") {
      upiPanel.classList.remove("hidden");
    }

    if (option.value === "card") {
      cardPanel.classList.remove("hidden");
    }

    if (option.value === "cod") {
      codPanel.classList.remove("hidden");
    }
  });
});

/* =========================================
        PROCESS PAYMENT
========================================= */

payButton.addEventListener("click", async () => {
  if (!orderId) {
    alert("Order not found.");

    return;
  }

  const selected = document.querySelector(
    'input[name="paymentMethod"]:checked',
  ).value;

  if (selected === "upi") {
    const upi = document.getElementById("upiId").value.trim();

    if (!upi) {
      alert("Please enter your UPI ID.");

      return;
    }
  }

  if (selected === "card") {
    const card = document.getElementById("cardNumber").value.trim();

    const expiry = document.getElementById("expiry").value.trim();

    const cvv = document.getElementById("cvv").value.trim();

    if (!card || !expiry || !cvv) {
      alert("Please complete your card details.");

      return;
    }
  }

  payButton.disabled = true;

  payButton.textContent = "Processing Secure Payment...";

  try {
    /*
            Create payment record.

            Adjust field names according
            to your PaymentSerializer.
        */

    const response = await fetch(`${API_BASE}/payments/`, {
      method: "POST",

      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify({
        order: Number(orderId),

        payment_method: selected,

        amount: Number(order.total),

        status: selected === "cod" ? "pending" : "paid",
      }),
    });

    if (!response.ok) {
      const error = await response.text();

      console.error(error);

      throw new Error("Payment could not be created.");
    }

    const payment = await response.json();

    console.log("PAYMENT CREATED:", payment);

    /*
            Successful payment/order
            → tracking page
        */

    window.location.href = `/tracking.html?order=${orderId}`;
  } catch (error) {
    console.error(error);

    alert("Payment failed. Please try again.");

    payButton.disabled = false;

    payButton.textContent = `Pay ₹${payAmount.textContent}`;
  }
});

/* =========================================
        GSAP
========================================= */

gsap.from(".payment-hero", {
  opacity: 0,

  y: 30,

  duration: 1,
});

gsap.from(".order-card, .payment-card", {
  opacity: 0,

  y: 40,

  stagger: 0.15,

  duration: 0.8,

  delay: 0.2,
});

loadOrder();
