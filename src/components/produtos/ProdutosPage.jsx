import React, { useEffect, useState } from "react";
import ListaDeProdutos from "./ListaDeProdutos";
import produtoService from "../../services/produtoService";
import { Alert, message } from "antd";

const ProdutosPage = () => {
  // Inicialize o carrinho de compras a partir do localStorage
  const [carrinho, setCarrinho] = useState(() => {
    const carrinhoSalvo = localStorage.getItem("carrinho");
    return carrinhoSalvo ? JSON.parse(carrinhoSalvo) : [];
  });

  const [messageApi, contextHolder] = message.useMessage();

  const success = () => {
    messageApi.open({
      type: "success",
      content: "Produto adicionado ao carrinho",
    });
  };

  const error = () => {
    messageApi.open({
      type: "error",
      content: "Estoque insuficiente",
    });
  };

  const [produtos, setProdutos] = useState([]); // State para armazenar os usuários

  const service = produtoService;

  useEffect(() => {
    async function fetchUsuarios() {
      try {
        const response = await service.getAllProdutos();
        setProdutos(response); // Define os usuários com os dados do serviço
      } catch (error) {
        console.error("Erro ao buscar usuários:", error);
      }
    }

    fetchUsuarios();
  }, []);

  const adicionarAoCarrinho = (produto) => {
    if (produto.quantidade === 0) {
      error();
    } else {
      // Crie uma cópia do carrinho atual e adicione o novo produto
      success();
      const novoCarrinho = [...carrinho, produto];

      // Atualize o carrinho com o novoCarrinho
      setCarrinho(novoCarrinho);

      // Atualize o carrinho no localStorage
      localStorage.setItem("carrinho", JSON.stringify(novoCarrinho));
    }
  };

  return (
    <div>
      {contextHolder}
      <h1>Lista de Produtos</h1>
      <ListaDeProdutos
        produtos={produtos}
        adicionarAoCarrinho={adicionarAoCarrinho}
      />
    </div>
  );
};

export default ProdutosPage;
