require 'rails_helper'

RSpec.describe Api::KeystrokeTypesController, type: :controller do
  describe "GET #index" do
    it "returns all keystroke types" do
      create_list :keystroke_type, 2

      get :index

      expect(json.length).to eq(2)
    end
  end

  describe "GET #show" do
    it "returns detail for one keystroke type" do
      keystroke_type = create :keystroke_type

      get :show, params: { id: keystroke_type.id }

      expect(json[:id]).to eq(keystroke_type.id)
      expect(json[:name]).to eq(keystroke_type.name)
    end
  end

  describe "POST #create" do
    it "creates a keystroke type" do
      post :create,
           params: { keystroke_type: { name: 'keystroke' } }

      expect(json).to include(:id)
      expect(json[:name]).to eq('keystroke')
    end
  end
end
