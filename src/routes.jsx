import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Menu from "./components/template/template";
import UserScreen from "./components/usuario/usuario";
import CartPage from "./components/carrinho/carrinho";
import usuarioService from "./services/usuarioService";
import ProdutosPage from "./components/produtos/ProdutosPage";

const listaUsuariosApi = await usuarioService.getAllUsuarios();

const AppRoutes = () => {
    return (
        <BrowserRouter>
            <Menu>
                <Routes>
                    <Route path="/" element={<ProdutosPage/>} />
                    <Route path="/usuario" element={<UserScreen ></UserScreen>} />
                    <Route path="/carrinho" element={<CartPage></CartPage>} />
                </Routes>
            </Menu>
        </BrowserRouter>
    );
};

export default AppRoutes;
