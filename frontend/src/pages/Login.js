function Login() {
  return (
    <div className="container">
      <h2>Faculty Login</h2>

      <input type="email" placeholder="Email" />

      <input type="password" placeholder="Password" />

      <button style={{ marginTop: "10px" }}>
        Login
      </button>
    </div>
  );
}

export default Login;