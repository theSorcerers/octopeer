require 'rails_helper'

RSpec.describe Api::FilePositionsController, type: :controller do
  describe "GET #index" do
    it "returns all file positions" do
      create_list :file_position, 2

      get :index

      expect(json.length).to eq(2)
    end
  end

  describe "GET #show" do
    it "returns detail for one file position" do
      file_position = create :file_position

      get :show, params: { id: file_position.id }

      expect(json[:id]).to eq(file_position.id)
      expect(json[:semantic_event][:id]).to eq(file_position.semantic_event_id)
      expect(json[:commit_hash]).to eq(file_position.commit_hash)
      expect(json[:filename]).to eq(file_position.filename)
      expect(json[:line_number]).to eq(file_position.line_number)
    end
  end

  describe "POST #create" do
    it "creates a file position" do
      semantic_event = create :semantic_event

      post :create,
           params: { file_position: { semantic_event_id: semantic_event.id,
                                      commit_hash: 'commithash',
                                      filename: 'filename',
                                      line_number: '42' } }

      expect(json).to include(:id)
      expect(json[:semantic_event][:id]).to eq(semantic_event.id)
      expect(json[:commit_hash]).to eq('commithash')
      expect(json[:filename]).to eq('filename')
      expect(json[:line_number]).to eq(42)
    end
  end
end
