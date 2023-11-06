import React, { useEffect, useState } from "react";
import ListaDeProdutos from "./ListaDeProdutos";

const produtos = [
  {
    id_produto: 1,
    nome_produto: "Smartphone Modelo X",
    descricao:
      "Um smartphone avançado com tela de alta resolução e câmera potente.",
    preco: 1200,
    estoque_disponivel: 50,
    url: "https://m.media-amazon.com/images/I/81cuxQCZFEL._AC_UF1000,1000_QL80_.jpg",
  },
  {
    id_produto: 2,
    nome_produto: "Camiseta Estampada",
    descricao: "Camiseta de algodão com estampa colorida.",
    preco: 25.99,
    estoque_disponivel: 100,
    url: "https://ae01.alicdn.com/kf/Sbbc292597dcc437ca945588e37e2615a6/Camiseta-Masculina-Anime-Monkey-D-Luffy-Estampada-3D-Top-de-Manga-Curta-Grande-Cartoon-Harajuku-Uma.jpg",
  },
  {
    id_produto: 3,
    nome_produto: "Arroz Integral 1kg",
    descricao: "Pacote de arroz integral de 1kg.",
    preco: 7.5,
    estoque_disponivel: 200,
    url: "https://carrefourbr.vtexassets.com/arquivos/ids/101741227/46b7c1249be8411f9c95070ffea62c6c.jpg?v=638120465221030000",
  },
  // Adicione os outros produtos aqui
];

const ProdutosPage = () => {
  // Inicialize o carrinho de compras a partir do localStorage
  const [carrinho, setCarrinho] = useState(() => {
    const carrinhoSalvo = localStorage.getItem("carrinho");
    return carrinhoSalvo ? JSON.parse(carrinhoSalvo) : [];
  });

  const adicionarAoCarrinho = (produto) => {
    // Crie uma cópia do carrinho atual e adicione o novo produto
    const novoCarrinho = [...carrinho, produto];

    // Atualize o carrinho com o novoCarrinho
    setCarrinho(novoCarrinho);

    // Atualize o carrinho no localStorage
    localStorage.setItem("carrinho", JSON.stringify(novoCarrinho));
  };

  return (
    <div>
      <h1>Lista de Produtos</h1>
      <ListaDeProdutos
        produtos={produtos}
        adicionarAoCarrinho={adicionarAoCarrinho}
      />
    </div>
  );
};

export default ProdutosPage;
