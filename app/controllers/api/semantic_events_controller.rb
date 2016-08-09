class Api::SemanticEventsController < ApplicationController
  include TimeHelper
  before_action :set_semantic_event, only: :show
  before_action only: :create do
    format_time(:semantic_event)
  end

  def index
    @semantic_events = SemanticEvent.all

    render json: @semantic_events
  end

  def show
    render json: @semantic_event
  end

  def create
    @semantic_event = SemanticEvent.new(semantic_event_params)

    if @semantic_event.save
      render json: @semantic_event, status: :created
    else
      render json: @semantic_event.errors, status: :unprocessable_entity
    end
  end

  private

  def set_semantic_event
    @semantic_event = SemanticEvent.find(params[:id])
  end

  def semantic_event_params
    params.require(:semantic_event).permit(:id, :session_id, :event_type_id, :element_type_id, :created_at)
  end
end
