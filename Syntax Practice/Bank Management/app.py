# Website version of the bank
# Run from this folder:  streamlit run app.py
# (the colours and font come from .streamlit/config.toml in this folder)

from html import escape

import streamlit as st
from bank import Bank, MIN_AGE, MAX_DEPOSIT

st.set_page_config(page_title="Bank Management", page_icon=":material/account_balance:", layout="centered")

# ---------- styling ----------
# Most colours come from the theme; this CSS only adds the passbook card,
# the details list and a few touch-ups Streamlit's theme can't do.
st.html("""
<style>
:root {
    --ledger: #13603D;
    --ledger-deep: #0B3D26;
    --brass: #C9A54C;
    --brass-hover: #D8B868;
    --page: #0D1712;
    --muted: #9DB0A5;
    --rule: #2B3D33;
    --surface: #14211B;
    --danger: #C4332B;
    --danger-hover: #A82A23;
}

/* brass buttons need dark text, white on brass is too low contrast */
[data-testid="stBaseButton-primary"],
[data-testid="stBaseButton-primaryFormSubmit"] {
    color: var(--page) !important;
    font-weight: 600;
}
[data-testid="stBaseButton-primary"]:hover,
[data-testid="stBaseButton-primaryFormSubmit"]:hover {
    background: var(--brass-hover) !important;
    border-color: var(--brass-hover) !important;
}

/* amounts line up when digits have equal width */
.passbook, [data-testid="stNumberInput"] input { font-variant-numeric: tabular-nums; }

[data-testid="stMainBlockContainer"] { padding-top: 3rem; }
h1 { font-weight: 600 !important; letter-spacing: -0.02em; }

/* forms sit on a raised surface instead of the page colour */
[data-testid="stForm"] { background: var(--surface); padding: 1.5rem; }

/* ---------- passbook card ---------- */
.passbook {
    background: var(--ledger);
    background-image: linear-gradient(160deg, var(--ledger) 0%, var(--ledger-deep) 100%);
    color: #F4F7F5;
    border-radius: 14px;
    padding: 10px;
    margin: 0;
}
.passbook .frame {
    border: 1px solid var(--brass);
    border-radius: 8px;
    padding: 1.4rem 1.6rem 1.3rem;
}
.passbook .bank {
    color: var(--brass);
    font-weight: 600;
    font-size: 0.95rem;
    letter-spacing: 0.02em;
}
.passbook .label { margin-top: 1.6rem; font-size: 0.9rem; opacity: 0.8; }
.passbook .amount {
    font-size: clamp(2.2rem, 7vw, 3.2rem);
    font-weight: 600;
    line-height: 1.1;
    letter-spacing: -0.02em;
}
.passbook .meta {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem 2.5rem;
    margin-top: 1.6rem;
    padding-top: 1rem;
    border-top: 1px solid rgba(201, 165, 76, 0.45);
}
.passbook .meta div { font-size: 0.85rem; opacity: 0.8; }
.passbook .meta strong { display: block; font-size: 1rem; font-weight: 500; opacity: 1; color: #FFFFFF; }

/* ---------- details list ---------- */
.details {
    background: var(--surface);
    border: 1px solid var(--rule);
    border-radius: 0.5rem;
    margin: 0;
    padding: 0;
}
.details .row {
    display: flex;
    justify-content: space-between;
    gap: 1rem;
    padding: 0.85rem 1.25rem;
    border-bottom: 1px solid var(--rule);
}
.details .row:last-child { border-bottom: none; }
.details .key { color: var(--muted); }
.details .value { font-weight: 500; text-align: right; overflow-wrap: anywhere; }

/* ---------- delete button in red ---------- */
.st-key-danger button {
    background: var(--danger) !important;
    border-color: var(--danger) !important;
    color: #FFFFFF !important;
}
.st-key-danger button:hover { background: var(--danger-hover) !important; }
</style>
""")


# ---------- helpers ----------

def inr(amount):
    # Indian grouping: 1234567 -> ₹12,34,567
    digits = str(abs(int(amount)))
    if len(digits) > 3:
        head, tail = digits[:-3], digits[-3:]
        groups = []
        while len(head) > 2:
            groups.insert(0, head[-2:])
            head = head[:-2]
        if head:
            groups.insert(0, head)
        digits = ",".join(groups) + "," + tail
    return ("-" if amount < 0 else "") + "\N{INDIAN RUPEE SIGN}" + digits


def notify(message):
    # remember a message, then rerun so the passbook card refreshes
    state.notice = message
    st.rerun()


def logout():
    state.accountNo = None
    state.pin = None


# Streamlit re-runs this whole file on every click, so data is reloaded from
# data.json each time and the logged-in user is kept in st.session_state.
bank = Bank()
state = st.session_state
state.setdefault("accountNo", None)
state.setdefault("pin", None)

if "notice" in state:
    st.toast(state.pop("notice"), icon=":material/check_circle:")


# ==================== not logged in ====================

if state.accountNo is None:
    st.title("Bank Management")
    st.write("Log in to deposit, withdraw and manage your account, or open a new one.")

    loginTab, createTab = st.tabs([":material/login: Log in", ":material/person_add: Open account"])

    with loginTab:
        with st.form("login"):
            accountNo = st.text_input("Account number")
            pin = st.text_input("PIN", type="password", max_chars=4)
            if st.form_submit_button("Log in", type="primary", icon=":material/login:", use_container_width=True):
                try:
                    account = bank.login(accountNo, pin)
                    state.accountNo, state.pin = account['account_no'], account['pin']
                    notify(f"Welcome back, {account['name']}")
                except ValueError as err:
                    st.error(err, icon=":material/error:")

    with createTab:
        with st.form("create"):
            name = st.text_input("Full name")
            email = st.text_input("E-mail")
            col1, col2 = st.columns(2)
            age = col1.number_input("Age", min_value=0, max_value=120, value=MIN_AGE, step=1,
                                    help=f"You must be {MIN_AGE} or older")
            pin = col2.text_input("Choose a PIN", type="password", max_chars=4, help="4 digits")
            if st.form_submit_button("Open account", type="primary", icon=":material/person_add:", use_container_width=True):
                try:
                    account = bank.createAccount(name, int(age), email, pin)
                    st.success("Account opened. Save your account number, you need it to log in.",
                               icon=":material/check_circle:")
                    st.code(account['account_no'], language=None)
                except ValueError as err:
                    st.error(err, icon=":material/error:")

    st.stop()


# ==================== logged in ====================

try:
    account = bank.login(state.accountNo, state.pin)
except ValueError:
    # account was deleted or PIN changed somewhere else
    logout()
    st.rerun()

# a horizontal container keeps the greeting and Log out on one row, even on phones
with st.container(horizontal=True, vertical_alignment="center", horizontal_alignment="distribute"):
    st.title(f"Hello, {account['name'].split()[0]}", width="content")
    st.button("Log out", on_click=logout, icon=":material/logout:", type="tertiary")

# every value is escaped because names and e-mails are typed by users
st.html(f"""
<div class="passbook" role="group" aria-label="Account summary">
  <div class="frame">
    <div class="bank">Bank Management</div>
    <div class="label">Available balance</div>
    <div class="amount">{inr(account['balance'])}</div>
    <div class="meta">
      <div>Account holder<strong>{escape(account['name'])}</strong></div>
      <div>Account number<strong>{escape(account['account_no'])}</strong></div>
    </div>
  </div>
</div>
""")

depositTab, withdrawTab, detailsTab, updateTab, deleteTab = st.tabs([
    ":material/add_circle: Deposit",
    ":material/remove_circle: Withdraw",
    ":material/badge: Details",
    ":material/edit: Edit details",
    ":material/delete: Close account",
])

with depositTab:
    with st.form("deposit", clear_on_submit=True):
        amount = st.number_input("Amount (\N{INDIAN RUPEE SIGN})", min_value=1, max_value=MAX_DEPOSIT - 1,
                                 value=None, step=100, placeholder="0",
                                 help=f"Up to {inr(MAX_DEPOSIT - 1)} per deposit")
        if st.form_submit_button("Deposit", type="primary", icon=":material/add:"):
            if amount is None:
                st.error("Enter an amount to deposit", icon=":material/error:")
            else:
                try:
                    balance = bank.deposit(state.accountNo, state.pin, int(amount))
                    notify(f"Deposited {inr(amount)}. New balance {inr(balance)}")
                except ValueError as err:
                    st.error(err, icon=":material/error:")

with withdrawTab:
    if account['balance'] == 0:
        st.info("Your balance is \N{INDIAN RUPEE SIGN}0. Deposit money first to withdraw it.",
                icon=":material/info:")
    else:
        with st.form("withdraw", clear_on_submit=True):
            amount = st.number_input("Amount (\N{INDIAN RUPEE SIGN})", min_value=1, max_value=account['balance'],
                                     value=None, step=100, placeholder="0",
                                     help=f"You can withdraw up to {inr(account['balance'])}")
            if st.form_submit_button("Withdraw", type="primary", icon=":material/remove:"):
                if amount is None:
                    st.error("Enter an amount to withdraw", icon=":material/error:")
                else:
                    try:
                        balance = bank.withdraw(state.accountNo, state.pin, int(amount))
                        notify(f"Withdrew {inr(amount)}. New balance {inr(balance)}")
                    except ValueError as err:
                        st.error(err, icon=":material/error:")

with detailsTab:
    rows = [
        ("Name", account['name']),
        ("Age", account['age']),
        ("E-mail", account['email']),
        ("Account number", account['account_no']),
        ("Balance", inr(account['balance'])),
    ]
    items = "".join(f'<div class="row"><span class="key">{label}</span>'
                    f'<span class="value">{escape(str(value))}</span></div>' for label, value in rows)
    st.html(f'<div class="details">{items}</div>')

with updateTab:
    with st.form("update", clear_on_submit=True):
        st.caption("Fill in only what you want to change. Empty fields stay as they are.")
        name = st.text_input("Name", placeholder=account['name'])
        email = st.text_input("E-mail", placeholder=account['email'])
        newPin = st.text_input("New PIN", type="password", max_chars=4, help="4 digits")
        if st.form_submit_button("Save changes", type="primary", icon=":material/save:"):
            if not (name or email or newPin):
                st.warning("Nothing to save. Fill in at least one field.", icon=":material/warning:")
            else:
                try:
                    updated = bank.updateDetails(state.accountNo, state.pin, name, email, newPin)
                    state.pin = updated['pin']      # stay logged in after a PIN change
                    notify("Changes saved")
                except ValueError as err:
                    st.error(err, icon=":material/error:")

with deleteTab:
    with st.form("delete"):
        st.write(f"Closing your account deletes it permanently, including the balance of "
                 f"**{inr(account['balance'])}**. Withdraw your money first.")
        confirmPin = st.text_input("Enter your PIN to confirm", type="password", max_chars=4)
        sure = st.checkbox("I understand this can't be undone")
        with st.container(key="danger"):
            submitted = st.form_submit_button("Close account", icon=":material/delete:")
        if submitted:
            if not sure:
                st.error("Tick the checkbox to confirm", icon=":material/error:")
            elif confirmPin != state.pin:
                st.error("That PIN is wrong", icon=":material/error:")
            else:
                bank.deleteAccount(state.accountNo, state.pin)
                logout()
                notify("Your account has been closed")
