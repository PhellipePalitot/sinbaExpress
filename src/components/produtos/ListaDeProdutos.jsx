import React, { useState } from "react";
import { Card, Col, Row, Input, Button } from "antd";
import FiltroDeProdutos from "../filtro/FiltroDeProdutos";

const { Meta } = Card;

const ListaDeProdutos = ({ produtos, adicionarAoCarrinho }) => {
  const [produtosFiltrados, setProdutosFiltrados] = useState([]);

  const handleAdicionarAoCarrinho = (produto) => {
    adicionarAoCarrinho(produto);
  };

  const handleFiltrar = (coluna, tipoComparacao, valorFiltro) => {
    // Crie uma cópia da lista original de produtos para evitar a modificação direta.
    let produtosFiltrados = [...produtos];

    // Verifique a opção selecionada para a coluna e aplique a lógica de filtragem correspondente.
    if (coluna && tipoComparacao && valorFiltro) {
      produtosFiltrados = produtosFiltrados.filter((produto) => {
        const valorColuna = produto[coluna];

        if (tipoComparacao === "contem" && typeof valorColuna === "string") {
          return valorColuna.includes(valorFiltro);
        } else if (tipoComparacao === "igual") {
          return valorColuna === valorFiltro;
        } else if (
          tipoComparacao === "maior_que" &&
          (typeof valorColuna === "number" || typeof valorColuna === "string")
        ) {
          return Number(valorColuna) > Number(valorFiltro);
        } else if (
          tipoComparacao === "menor_que" &&
          (typeof valorColuna === "number" || typeof valorColuna === "string")
        ) {
          return Number(valorColuna) < Number(valorFiltro);
        }

        return false; // Não corresponde a nenhum critério
      });
    }

    setProdutosFiltrados(produtosFiltrados);
  };

  const cardStyle = {
    width: 350,
    height: 400,
    marginBottom: 10,
  };

  const imageStyle = {
    height: 160,
    objectFit: "cover",
  };

  const buttonStyle = {
    marginTop: "10px", // Adicione um espaçamento entre a descrição e o botão
  };

  return (
    <div>
      <div style={{ marginBottom: 30, marginTop: 10 }}>
        <FiltroDeProdutos produtos={produtos} onFiltrar={handleFiltrar} />
      </div>
      <Row gutter={16}>
        {produtosFiltrados.length
          ? produtosFiltrados.map((produto) => (
              <Col key={produto.nome_produto} span={6}>
                <Card
                  hoverable
                  style={cardStyle}
                  cover={
                    <img
                      alt={produto.nome_produto}
                      src={produto.url}
                      style={imageStyle}
                    />
                  }
                >
                  <Meta
                    title={produto.nome_produto}
                    description={produto.descricao}
                  />
                  <div>
                    <p>Preço: R$ {produto.preco}</p>
                  </div>
                  <Button
                    style={buttonStyle}
                    onClick={() => handleAdicionarAoCarrinho(produto)}
                  >
                    Adicionar ao Carrinho
                  </Button>
                </Card>
              </Col>
            ))
          : produtos.map((produto) => (
              <Col key={produto.nome_produto} span={6}>
                <Card
                  hoverable
                  style={cardStyle}
                  cover={
                    <img
                      alt={produto.nome_produto}
                      src={produto.url}
                      style={imageStyle}
                    />
                  }
                >
                  <Meta
                    title={produto.nome_produto}
                    description={produto.descricao}
                  />
                  <div>
                    <p>Preço: R$ {produto.preco}</p>
                  </div>
                  <Button
                    style={buttonStyle}
                    onClick={() => handleAdicionarAoCarrinho(produto)}
                  >
                    Adicionar ao Carrinho
                  </Button>
                </Card>
              </Col>
            ))}
      </Row>
    </div>
  );
};

export default ListaDeProdutos;
