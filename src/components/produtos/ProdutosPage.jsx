import React from "react";
import ListaDeProdutos from "./ListaDeProdutos";

const produtos = [
  {
    nome_produto: "Smartphone Modelo X",
    descricao:
      "Um smartphone avançado com tela de alta resolução e câmera potente.",
    preco: 1200,
    estoque_disponivel: 50,
    url: "https://m.media-amazon.com/images/I/81cuxQCZFEL._AC_UF1000,1000_QL80_.jpg",
  },
  {
    nome_produto: "Camiseta Estampada",
    descricao: "Camiseta de algodão com estampa colorida.",
    preco: 25.99,
    estoque_disponivel: 100,
    url: "https://ae01.alicdn.com/kf/Sbbc292597dcc437ca945588e37e2615a6/Camiseta-Masculina-Anime-Monkey-D-Luffy-Estampada-3D-Top-de-Manga-Curta-Grande-Cartoon-Harajuku-Uma.jpg",
  },
  {
    nome_produto: "Arroz Integral 1kg",
    descricao: "Pacote de arroz integral de 1kg.",
    preco: 7.5,
    estoque_disponivel: 200,
    url: "https://carrefourbr.vtexassets.com/arquivos/ids/101741227/46b7c1249be8411f9c95070ffea62c6c.jpg?v=638120465221030000",
  },
  // Adicione os outros produtos aqui
];

const ProdutosPage = () => {
  return (
    <div>
      <h1>Lista de Produtos</h1>
      <ListaDeProdutos produtos={produtos} />
    </div>
  );
};

export default ProdutosPage;
