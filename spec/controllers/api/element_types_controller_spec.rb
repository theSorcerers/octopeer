require 'rails_helper'

RSpec.describe Api::ElementTypesController, type: :controller do
  describe "GET #index" do
    it "returns all element types" do
      create_list :element_type, 2

      get :index

      expect(json.length).to eq(2)
    end
  end

  describe "GET #show" do
    it "returns detail for one element type" do
      element_type = create :element_type

      get :show, params: { id: element_type.id }

      expect(json[:id]).to eq(element_type.id)
      expect(json[:name]).to eq(element_type.name)
    end
  end

  describe "POST #create" do
    it "creates a element type" do
      post :create,
           params: { element_type: { name: 'element' } }

      expect(json).to include(:id)
      expect(json[:name]).to eq('element')
    end
  end
end
