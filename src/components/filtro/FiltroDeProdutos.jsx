import React, { useState } from "react";
import { Select, Input, Button, Space } from "antd";

const { Option } = Select;

const FiltroDeProdutos = ({ produtos, onFiltrar }) => {
  const [coluna, setColuna] = useState("");
  const [tipoComparacao, setTipoComparacao] = useState("");
  const [valorFiltro, setValorFiltro] = useState("");

  const handleFiltrar = () => {
    onFiltrar(coluna, tipoComparacao, valorFiltro);
  };

  return (
    <div>
      <Space>
        <Select
          style={{ width: 150 }}
          placeholder="Selecione uma coluna"
          onChange={(value) => setColuna(value)}
        >
          <Option value="nome_produto">Nome do Produto</Option>
          <Option value="descricao">Descrição</Option>
          <Option value="preco">Preço</Option>
          <Option value="estoque_disponivel">Estoque Disponível</Option>
        </Select>
        <Select
          style={{ width: 150 }}
          placeholder="Selecione a comparação"
          onChange={(value) => setTipoComparacao(value)}
        >
          <Option value="contem">Contém</Option>
          <Option value="igual">Igual</Option>
          <Option value="maior_que">Maior que</Option>
          <Option value="menor_que">Menor que</Option>
        </Select>
        <Input
          style={{ width: 150 }}
          placeholder="Valor"
          value={valorFiltro}
          onChange={(e) => setValorFiltro(e.target.value)}
        />
        <Button type="primary" onClick={handleFiltrar}>
          Filtrar
        </Button>
      </Space>
    </div>
  );
};

export default FiltroDeProdutos;
