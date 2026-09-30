import {BrowserRouter as Router, Route, Routes} from 'react-router-dom';
import ProductList from "./pages/ProductList";
import ProductDetails from "./pages/ProductDetails";
import CartPage from "./pages/CartPage";
import Navbar from "./components/Navbar.jsx";
import CheckoutPage from './pages/CheckoutPage';
function App() {
    return (
        <Router>
            <Navbar/>
            <Routes>
                <Route path="/" element={<ProductList/>}/>
                <Route path="/product/:id" element={<ProductDetails/>}/>
                <Route path="/cart" element={<CartPage/>}/>
                <Route path="/checkout" element={<CheckoutPage/>}/>
            </Routes>
        </Router>
    );
}

export default App;