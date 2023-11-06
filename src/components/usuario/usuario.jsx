import React, { useState, useEffect } from "react";
import { Card, Typography, Input } from "antd";
import ListaDeUsuarios from "./listaDeUsuarios";
import usuarioService from "../../services/usuarioService"; // Importe o serviço

const { Title, Text } = Typography;
const { Search } = Input;

const UserProfile = () => {
  const [usuarios, setUsuarios] = useState([]); // State para armazenar os usuários
  const [filtro, setFiltro] = useState(""); // State para o filtro de pesquisa
  const [usuariosFiltrados, setUsuariosFiltrados] = useState([]); // State para armazenar os usuários

  const service = usuarioService;

  useEffect(() => {
    async function fetchUsuarios() {
      try {
        const response = await service.getAllUsuarios();
        localStorage.setItem('clientes', JSON.stringify(response));
        setUsuarios(response); // Define os usuários com os dados do serviço
      } catch (error) {
        console.error("Erro ao buscar usuários:", error);
      }
    }

    fetchUsuarios();
  }, []);

  const filtrarUsuarios = (filtro) => {
    if (filtro.trim() === "") {
      // Se o filtro estiver vazio, redefina a lista de usuários para a lista original
      setFiltro("");
      setUsuariosFiltrados([]);
    } else {
      // Filtrar usuários com base no filtro de pesquisa
      const usuariosFiltrados = usuarios.filter((usuario) => {
        // Verifique se qualquer valor de coluna contém o filtro de pesquisa (ignorando maiúsculas e minúsculas)
        for (const key in usuario) {
          if (usuario[key].toString().toLowerCase().includes(filtro.toLowerCase())) {
            return true;
          }
        }
        return false;
      });

      setFiltro(filtro);
      setUsuariosFiltrados(usuariosFiltrados);
    }
  };

  return (
    <div>
      <Search
        placeholder="Pesquisar usuários"
        onSearch={filtrarUsuarios}
        enterButton
      />
      <ListaDeUsuarios listaUsuarios={usuariosFiltrados.length ? usuariosFiltrados : usuarios} />
    </div>
  );
};

export default UserProfile;
