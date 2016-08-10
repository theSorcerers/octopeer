class Api::SemanticEventsController < ApplicationController
  include TimeHelper
  include Showable
  include Indexable
  include Createable

  private

  def semantic_event_params
    params.require(:semantic_event).permit(:id, :session_id, :event_type_id, :element_type_id, :created_at)
  end
end
