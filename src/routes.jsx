import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Menu from "./components/template/template";
import UserScreen from "./components/usuario/usuario";
import CartPage from "./components/carrinho/carrinho";

const AppRoutes = () => {
    return (
        <BrowserRouter>
            <Menu>
                <Routes>
                    <Route path="/usuario" element={<UserScreen></UserScreen>} />
                    <Route path="/carrinho" element={<CartPage></CartPage>} />
                </Routes>
            </Menu>
        </BrowserRouter>
    );
};

export default AppRoutes;
