import React, { useState } from "react";
import { Card, Col, Row, Input, Button } from "antd";
import FiltroDeProdutos from "../filtro/FiltroDeProdutos";

const { Meta } = Card;

const ListaDeProdutos = ({ produtos, adicionarAoCarrinho }) => {
    const [produtosFiltrados, setProdutosFiltrados] = useState(produtos);

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
            } else if (tipoComparacao === "maior_que" && (typeof valorColuna === "number" || typeof valorColuna === "string")) {
              return Number(valorColuna) > Number(valorFiltro);
            } else if (tipoComparacao === "menor_que" && (typeof valorColuna === "number" || typeof valorColuna === "string")) {
              return Number(valorColuna) < Number(valorFiltro);
            }
      
            return false; // Não corresponde a nenhum critério
          });
        }
      
        setProdutosFiltrados(produtosFiltrados);
      };

  return (
    <div>
        <div style={{marginBottom: 30}}>

      <FiltroDeProdutos produtos={produtos} onFiltrar={handleFiltrar} />
        </div>
      <Row gutter={16}>
        {produtosFiltrados.map((produto) => (
          <Col key={produto.nome_produto} span={6}>
            <Card
              hoverable
              style={{ width: 240 }}
              cover={
                <img alt={produto.nome_produto} src={produto.url} />
              }
            >
              <Meta
                title={produto.nome_produto}
                description={produto.descricao}
              />
              <div>
                <p>Preço: R$ {produto.preco}</p>
                <Button onClick={() => handleAdicionarAoCarrinho(produto)}>
                  Adicionar ao Carrinho
                </Button>
              </div>
            </Card>
          </Col>
        ))}
      </Row>
    </div>
  );
};

export default ListaDeProdutos;
